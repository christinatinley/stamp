from mistralai import Mistral
from langchain_mistralai.embeddings import MistralAIEmbeddings
import numpy as np
import faiss
import os
from dotenv import load_dotenv
from knowledge_base import k_b
import torch
import requests
import time
from requests.exceptions import RequestException

# temp workaround
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

# Load API key and set up environment
load_dotenv()
api_key = os.getenv('MISTRAL_API_KEY')

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

client = Mistral(api_key=api_key)
embeddings_model = MistralAIEmbeddings(model="mistral-embed", mistral_api_key=api_key)

VECTOR_DB = []
FOOD_VECTOR_DB = []

# Function to embed a chunk of text
def embed_chunk(text):
    embedding = embeddings_model.embed_query(text)
    return np.array(embedding) 

def embed_chunks_local(chunks):
    embeddings_batch_response = client.embeddings.create(
        model="mistral-embed",
        inputs=chunks
    )
    return [embedding.embedding for embedding in embeddings_batch_response.data]


# Function to add a chunk to the database (embeds it and stores the text)
def add_chunk_to_database(place_data_list, itinerary, food=False):
    chunks = []

    existing_names = {
        line.split("Place Name: ")[1].split("\n")[0]
        for line in itinerary
        if "Place Name: " in line
    }

    existing_coords = {
        (line.split("Latitude: ")[1].split("\n")[0], line.split("Longitude: ")[1].split("\n")[0])
        for line in itinerary
        if "Latitude: " in line and "Longitude: " in line
    }

    for place_data in place_data_list:
        name_data = place_data.get('displayName', {'text': 'No Name'})
        name = name_data.get('text', 'No Name') if isinstance(name_data, dict) else str(name_data)

        address = place_data.get('formatted_address', 'No Address')
        rating = place_data.get('rating', 'No Rating')
        review = place_data.get('reviews', ['No Review'])[0]
        types = place_data.get('types', ['No Type'])

        location_data = place_data.get('location', {'latitude': 'No Latitude', 'longitude': 'No Longitude'})
        lat = location_data.get('latitude', 'No Latitude')
        lng = location_data.get('longitude', 'No Longitude')

        chunk = f"""Place Name: {name}
    Address: {address}
    Rating: {rating}
    Reviews: {review}
    Types: {', '.join(types)}
    Latitude: {lat}
    Longitude: {lng}"""

        if name not in existing_names and (str(lat), str(lng)) not in existing_coords:
            chunks.append(chunk)
            existing_names.add(name)
            existing_coords.add((str(lat), str(lng)))

    embeddings = embed_chunks_local(chunks)
    if food:
        for embedding, chunk in zip(embeddings, chunks):
            FOOD_VECTOR_DB.append((embedding, chunk))
    else:
        for embedding, chunk in zip(embeddings, chunks):
            VECTOR_DB.append((embedding, chunk))

# Function to build a FAISS index from the stored vectors
def build_faiss_index(food=False):
    vectors_raw = [vec for vec, _ in VECTOR_DB] if not food else [vec for vec, _ in FOOD_VECTOR_DB]

    for i, vec in enumerate(vectors_raw):
        if not isinstance(vec, (list, np.ndarray)):
            raise ValueError(f"Vector at index {i} is not a list or array: {vec}")
        if isinstance(vec, list) and any(isinstance(sub, (list, tuple)) for sub in vec):
            raise ValueError(f"Vector at index {i} is nested: {vec}")

    vectors = np.array(vectors_raw, dtype=np.float32)

    if len(vectors) == 0:
        raise ValueError("No vectors to build FAISS index.")

    dimension = vectors.shape[1]
    if dimension != 1024:
        raise ValueError(f"Expected dimension 1024, but got {dimension}")

    index = faiss.IndexFlatL2(dimension)
    faiss.normalize_L2(vectors)
    index.add(vectors)

    return index


# Function to retrieve the top N results based on a query
def retrieve(query, index, top_n=5, food=False):
    query_embedding = embed_chunk(query)
    query_embedding = query_embedding / np.linalg.norm(query_embedding)
    distances, indices = index.search(np.array([query_embedding]), top_n)
    results = [VECTOR_DB[i][1] for i in indices[0]] if not food else [FOOD_VECTOR_DB[i][1] for i in indices[0]]
    return results

# Function to build the places database
def build_places(cty_name, price_level, itinerary):
    lat, lng = k_b.get_city(cty_name)
    places = k_b.get_all_places(lat, lng, 1000, price_level)
    add_chunk_to_database(places, itinerary)
    food_places = k_b.get_food(lat, lng, 1000, price_level)
    add_chunk_to_database(food_places, itinerary, food=True)
    return lat, lng

# Function to generate an itinerary based on city and other preferences
def generate_itinerary(city_name, start_time, lat, lng, culture, history, art, nature, walking_tours, shopping, itinerary):
    global VECTOR_DB
    index = build_faiss_index()
        
    excluded_places = []
    for place in itinerary:
        name = place.split("Place Name: ")[1].split("\n")[0]
        lat = place.split("Latitude: ")[1].split("\n")[0]
        lng = place.split("Longitude: ")[1].split("\n")[0]
        excluded_places.append(f"{name} (Latitude: {lat}, Longitude: {lng})")

    excluded_places_str = ", ".join(excluded_places)
    query = f"""You are a travel agent helping me develop an itinerary for my trip to {city_name}. I am trying to find an activity for {start_time.strftime("%Y-%m-%d %H:%M")}. I have some preferences for the types of activities I would like to do, but I am open to suggestions. I am not interested in visiting any of the following places again: {excluded_places_str}.
These are all the places I am already visiting. Do not pick any of these locations a second time: {excluded_places_str}.
I am visiting {city_name}.
I want to experience a variety of activities, but I have some preferences in how much I would like to visit each activity.

This is how much I want to experience each of the following categories: 
culture: {culture / 10}
history: {history / 10}
art: {art / 10}
nature: {nature / 10}
walking tours: {walking_tours / 10}
shopping: {shopping / 10}
Although I have some preferences, I want to visit different places in {city_name}"""

    results = retrieve(query, index, top_n=1)
    selected_text = results[0]
    VECTOR_DB = [entry for entry in VECTOR_DB if entry[1] != selected_text]

    return selected_text

def generate_food(city_name, start_time):
    global FOOD_VECTOR_DB
    print("Yummy in my tummy")
    index = build_faiss_index(food=True)
    query = f"""You are a travel agent helping me develop an itinerary for my trip to {city_name}. I am trying to find a restaurant to go to at {start_time.strftime("%Y-%m-%d %H:%M")}. Please choose something good!"""
    
    results = retrieve(query, index, top_n=1, food=True)
    selected_text = results[0]
    print(selected_text)
    FOOD_VECTOR_DB = [entry for entry in FOOD_VECTOR_DB if entry[1] != selected_text]
    
    return selected_text
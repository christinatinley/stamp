from mistralai import Mistral
from langchain_mistralai.embeddings import MistralAIEmbeddings
import numpy as np
import faiss
import os
from dotenv import load_dotenv
from knowledge_base import k_b
import torch
import requests

# temp workaround
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

# Load API key and set up environment
load_dotenv()
api_key = os.getenv('MISTRAL_API_KEY')

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

client = Mistral(api_key=api_key)
embeddings_model = MistralAIEmbeddings(model="mistral-embed", mistral_api_key=api_key)

VECTOR_DB = []

# Function to embed a chunk of text
def embed_chunk(text):
    embedding = embeddings_model.embed_query(text)
    return np.array(embedding) 

# Function to embed multiple chunks of text
def embed_chunks(chunks):
    url = "https://api.mistral.ai/v1/embeddings"
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistral-embed",
        "input": chunks
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise error for bad HTTP responses
        response_data = response.json()

        embeddings = response_data.get("data", [])
        if not embeddings:
            raise ValueError("No embeddings found in response.")
        
        # Ensure that embeddings are returned as a list of numeric values (not dicts)
        return [embedding.get("embedding", []) for embedding in embeddings]
    
    except requests.exceptions.RequestException as e:
        print(f"Error with the API request: {e}")
        return []

# Function to add a chunk to the database (embeds it and stores the text)
def add_chunk_to_database(place_data_list, itinerary):
    chunks = []
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

        # Create a chunk of text containing the place's details
        chunk = f"""Place Name: {name}
    Address: {address}
    Rating: {rating}
    Reviews: {review}
    Types: {', '.join(types)}
    Latitude: {lat}
    Longitude: {lng}"""

    # Build a set of names already in the itinerary
    existing_names = {
        line.split("Place Name: ")[1].split("\n")[0]
        for line in itinerary
        if "Place Name: " in line
    }
    if name not in existing_names:
        chunks.append(chunk)

    # Embed the chunks and add to database
    embeddings = embed_chunks(chunks)
    for embedding, chunk in zip(embeddings, chunks):
        VECTOR_DB.append((embedding, chunk))  # Store the embedding and the corresponding chunk

# Function to build a FAISS index from the stored vectors
def build_faiss_index():
    # Convert the vectors to a numpy array with float32 type
    vectors = np.array([vec for vec, _ in VECTOR_DB], dtype=np.float32)

    # If there are no vectors, raise an error
    if len(vectors) == 0:
        raise ValueError("No vectors to build FAISS index.")
    
    dimension = vectors.shape[1]  # Get the embedding dimension (number of features per vector)

    # Check if all vectors have the correct dimension
    if dimension != 1024:  # Adjust to match your model's output dimension
        raise ValueError(f"Expected dimension 1024, but got {dimension}")

    # Create a FAISS index based on L2 distance (Euclidean distance)
    index = faiss.IndexFlatL2(dimension)
    
    # Normalize vectors using FAISS (ensure they are unit vectors)
    faiss.normalize_L2(vectors)  # This normalizes the vectors in-place
    
    # Add vectors to the index
    index.add(vectors)
    
    return index

# Function to retrieve the top N results based on a query
def retrieve(query, index, top_n=5):
    query_embedding = embed_chunk(query)
    query_embedding = query_embedding / np.linalg.norm(query_embedding)  # Normalize query
    distances, indices = index.search(np.array([query_embedding]), top_n)
    results = [VECTOR_DB[i][1] for i in indices[0]]  # Return the corresponding chunks
    return results

# Function to build the places database
def build_places(lat, lng, price_level, itinerary):
    places = k_b.get_all_places(lat, lng, 1000, price_level)
    add_chunk_to_database(places, itinerary)
    
def generate_first(city_name, days, culture, history, art, nature, walking_tours, shopping, price_level, itinerary):
    lat, lng = k_b.get_city(city_name)  # Get latitude and longitude for the city
    return generate_itinerary(city_name, lat, lng, days, culture, history, art, nature, walking_tours, shopping, price_level, itinerary)

# Function to generate an itinerary based on city and other preferences
def generate_itinerary(city_name, lat, lng, days, culture, history, art, nature, walking_tours, shopping, price_level, itinerary):
    build_places(lat, lng, price_level, itinerary)  # Build the places database for the city
    index = build_faiss_index()  # Build the FAISS index for place embeddings
    
    excluded_places = []
    for place in itinerary:
        name = place.split("Place Name: ")[1].split("\n")[0]  # Extract place name
        lat = place.split("Latitude: ")[1].split("\n")[0]  # Extract latitude
        lng = place.split("Longitude: ")[1].split("\n")[0]  # Extract longitude
        excluded_places.append(f"{name} (Latitude: {lat}, Longitude: {lng})")

    # Build the query to exclude the places already in the itinerary
    excluded_places_str = ", ".join(excluded_places)
    query = f"""You are a travel agent helping me develop an itinerary for my trip to {city_name}. 
These are all the places I am already visiting. Do not pick any of these locations a second time: {excluded_places_str}.
I am visiting {city_name} for {days} days.
I want to experience a variety of activities, but I have some preferences in how much I would like to visit each activity.

This is how much I want to experience each of the following categories: 
culture: {culture / 10}
history: {history / 10}
art: {art / 10}
nature: {nature / 10}
walking tours: {walking_tours / 10}
shopping: {shopping / 10}
Although I have some preferences, I want to visit different places in {city_name}"""
    
    # Retrieve the top N places based on the query
    results = retrieve(query, index, top_n=1)
    return results[0]

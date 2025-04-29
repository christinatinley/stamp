from mistralai import Mistral
import numpy as np
import faiss
import os
from dotenv import load_dotenv
from knowledge_base import k_b
import torch

load_dotenv()
api_key = os.getenv('MISTRAL_API_KEY')

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

client = Mistral(api_key=api_key)

VECTOR_DB = []

def embed_chunk(text):
    response = client.embed(texts=[text]) 
    embedding = response['embeddings'][0]
    return np.array(embedding)

def add_chunk_to_database(place_data):
    name = place_data.get('name', 'No Name')
    address = place_data.get('formatted_address', 'No Address')
    rating = place_data.get('rating', 'No Rating')
    types = place_data.get('types', [])
    review = place_data.get('review', ['No Review'])[0]
  
    chunk =  f"""Place Name: {name}
Address: {address}
Rating: {rating}
Types: {', '.join(types)}
Review: "{review}"
"""
    embedding = embed_chunk(chunk)
    VECTOR_DB.append((embedding, chunk))

def build_faiss_index():
    dimension = len(VECTOR_DB[0][0])
    index = faiss.IndexFlatL2(dimension)
    vectors = np.array([vec for vec, _ in VECTOR_DB])
    faiss.normalize_L2(vectors)
    index.add(vectors)
    return index

def retrieve(query, index, top_n=3):
    query_embedding = embed_chunk(query)
    query_embedding = query_embedding / np.linalg.norm(query_embedding)
    distances, indices = index.search(np.array([query_embedding]), top_n)
    results = [VECTOR_DB[i][1] for i in indices[0]]
    return results

def build_places(lat, lng):
    places = k_b.get_places(lat, lng, 100)
    for p in places:
        add_chunk_to_database(p)

def generate_itinerary(city_name, days, culture, history, art, nature, walking_tours, shopping):
    lat, lng = k_b.get_city(city_name) 
    build_places(lat, lng)
    index = build_faiss_index()
    query = f"""Generate a {days}-day itinerary for {city_name}. 
        This is how much I want to experience each of the following categories: 
        culture: {culture}/10
        history: {history}/10
        art: {art}/10
        nature: {nature}/10
        walking tours: {walking_tours}/10
        shopping: {shopping}/10
        When choosing a place, check to see if it is already in the itinerary. If it is, pick another activity."""
    results = retrieve(query, index, top_n=3)
    itinerary = [chunk for chunk in results]
    return itinerary

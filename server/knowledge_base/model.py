from mistralai import Mistral
from langchain_mistralai.embeddings import MistralAIEmbeddings
import numpy as np
import faiss
import os
from dotenv import load_dotenv
from knowledge_base import k_b
import torch

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
    return np.array(embedding)  # Ensure it's a numpy array

# Function to add a chunk to the database (embeds it and stores the text)
def add_chunk_to_database(place_data):
    name = place_data.get('displayName', 'No Name')
    address = place_data.get('formatted_address', 'No Address')
    rating = place_data.get('rating', 'No Rating')
    review = place_data.get('reviews', ['No Review'])[0]
    types = place_data.get('types', ['No Type'])
  
    # Create a chunk of text containing the place's details
    chunk = f"""Place Name: {name}
Address: {address}
Rating: {rating}
Reviews: {review}
Types: {', '.join(types)}
"""
    # Embed the chunk and add to the database
    embedding = embed_chunk(chunk)
    VECTOR_DB.append((embedding, chunk))

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
def build_places(lat, lng):
    places = k_b.get_places(lat, lng, 10)['places']
    for i,p in enumerate(places):
        print("Adding next chunk...", i)
        add_chunk_to_database(p)

# Function to generate an itinerary based on city and other preferences
def generate_itinerary(city_name, days, culture, history, art, nature, walking_tours, shopping):
    lat, lng = k_b.get_city(city_name)  # Get coordinates for the city
    build_places(lat, lng)  # Build the places database for the city
    index = build_faiss_index()  # Build the FAISS index for place embeddings
    
    # Formulate the query for generating the itinerary
    query = f"""Generate a {days}-day itinerary for {city_name}. 
    This is how much I want to experience each of the following categories: 
    culture: {culture}/10
    history: {history}/10
    art: {art}/10
    nature: {nature}/10
    walking tours: {walking_tours}/10
    shopping: {shopping}/10
    When choosing a place, check to see if it is already in the itinerary. If it is, pick another activity."""
    
    # Retrieve the top N places based on the query
    results = retrieve(query, index, top_n=3*days)
    itinerary = [chunk for chunk in results]  # Get the chunks corresponding to the top results
    print("Generated itinerary:")
    for i in itinerary:
        print(i)
    return itinerary

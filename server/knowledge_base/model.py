import ollama
import knowledge_base

EMBEDDING_MODEL = 'hf.co/CompendiumLabs/bge-base-en-v1.5-gguf'
LANGUAGE_MODEL = None # load minstrel here

# Each element in the VECTOR_DB will be a tuple (chunk, embedding)
# The embedding is a list of floats, for example: [0.1, 0.04, -0.34, 0.21, ...]
VECTOR_DB = []

def add_chunk_to_database(chunk):
  embedding = ollama.embed(model=EMBEDDING_MODEL, input=chunk)['embeddings'][0]
  VECTOR_DB.append((chunk, embedding))

def build_itinerary(city_name):
    lat, lng = knowledge_base.get_city(city_name)
    places = knowledge_base.get_places(lat, lng)
    for p in places:
        add_chunk_to_database(p)

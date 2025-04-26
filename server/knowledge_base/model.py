import ollama
import knowledge_base

EMBEDDING_MODEL = 'hf.co/CompendiumLabs/bge-base-en-v1.5-gguf'
LANGUAGE_MODEL = None # load minstrel here

VECTOR_DB = []

def add_chunk_to_database(chunk):
  embedding = ollama.embed(model=EMBEDDING_MODEL, input=chunk)['embeddings'][0]
  VECTOR_DB.append((chunk, embedding))

def build_itinerary(lat, lng):
    places = knowledge_base.get_places(lat, lng, 100)
    for p in places:
        add_chunk_to_database(p)

def cosine_similarity(a, b):
  dot_product = sum([x * y for x, y in zip(a, b)])
  norm_a = sum([x ** 2 for x in a]) ** 0.5
  norm_b = sum([x ** 2 for x in b]) ** 0.5
  return dot_product / (norm_a * norm_b)

def retrieve(query, top_n=3):
  query_embedding = ollama.embed(model=EMBEDDING_MODEL, input=query)['embeddings'][0] 
  similarities = []
  for chunk, embedding in VECTOR_DB:
    similarity = (chunk, cosine_similarity(query_embedding, embedding))
    similarities.append(similarity)
  similarities.sort(key=lambda x: x[1], reverse=True)
  return similarities[:top_n]
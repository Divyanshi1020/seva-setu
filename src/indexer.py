import pandas as pd
import chromadb
from sentence_transformers import SentenceTransformer
import os

print("Seva Setu — Building Search Engine")
print("=" * 50)

# Load your multilingual dataset
df = pd.read_csv('data/processed/schemes_multilingual.csv')
print(f"Loaded {len(df)} schemes")

# Load MuRIL model
print("\nLoading MuRIL model...")
model = SentenceTransformer('google/muril-base-cased')
print("Model loaded!")

# Create ChromaDB database
print("\nCreating vector database...")
client = chromadb.PersistentClient(path="./chroma_db")

# Delete existing collection if rebuilding
try:
    client.delete_collection("seva_setu_schemes")
    print("Cleared existing database")
except:
    pass

collection = client.create_collection(
    name="seva_setu_schemes",
    metadata={"hnsw:space": "cosine"}
)

# Create search documents from each scheme
# We combine all important fields into one searchable text
print("\nPreparing documents for indexing...")
documents = []
metadatas = []
ids = []

for _, row in df.iterrows():
    # This is what gets searched — rich combined text
    search_doc = f"""
    Service Name: {row['service_name']}
    Category: {row['category']}
    Ministry: {row['ministry']}
    Description: {row['description']}
    Eligibility: {row['eligibility']}
    How to Apply: {row['how_to_apply']}
    Documents Required: {row['documents']}
    """.strip()
    
    documents.append(search_doc)
    
    metadatas.append({
        'service_id': str(row['service_id']),
        'service_name': str(row['service_name']),
        'ministry': str(row['ministry']),
        'category': str(row['category']),
        'portal_url': str(row['portal_url']),
        'eligibility': str(row['eligibility']),
        'how_to_apply': str(row['how_to_apply']),
        'documents': str(row['documents'])
    })
    
    ids.append(str(row['service_id']))

# Generate embeddings using MuRIL
print(f"\nGenerating embeddings for {len(documents)} schemes...")
print("This takes 1-2 minutes...")
embeddings = model.encode(
    documents,
    batch_size=16,
    show_progress_bar=True,
    normalize_embeddings=True
)

# Store everything in ChromaDB
print("\nIndexing into vector database...")
collection.add(
    embeddings=embeddings.tolist(),
    documents=documents,
    metadatas=metadatas,
    ids=ids
)

print(f"\n✓ Successfully indexed {collection.count()} schemes")
print("✓ Vector database saved to ./chroma_db")
print("\nNext: Run search_test.py to test the search engine")
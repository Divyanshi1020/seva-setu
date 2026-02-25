import chromadb
from sentence_transformers import SentenceTransformer
from langdetect import detect

print("Seva Setu — Search Engine Test")
print("=" * 50)

# Load model and database
model = SentenceTransformer('google/muril-base-cased')
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection("seva_setu_schemes")

def search(query, n_results=3):
    # Detect language
    try:
        lang = detect(query)
    except:
        lang = 'en'
    
    # Convert query to vector
    query_vector = model.encode(query, normalize_embeddings=True)
    
    # Search database
    results = collection.query(
        query_embeddings=[query_vector.tolist()],
        n_results=n_results
    )
    
    print(f"\nQuery: '{query}'")
    print(f"Detected Language: {lang}")
    print(f"Top Results:")
    print("-" * 40)
    
    for i in range(len(results['metadatas'][0])):
        meta = results['metadatas'][0][i]
        score = 1 - results['distances'][0][i]
        print(f"{i+1}. {meta['service_name']}")
        print(f"   Category : {meta['category']}")
        print(f"   Relevance: {score:.0%}")
        print(f"   Apply at : {meta['portal_url']}")
        print()

# Test in multiple languages
search("farmer income support scheme")
search("किसान को पैसे देने वाली योजना")
search("விவசாயிகளுக்கு பணம் தரும் திட்டம்")
search("health insurance for poor families")
search("घर बनाने के लिए सरकारी मदद")
search("free education for children")
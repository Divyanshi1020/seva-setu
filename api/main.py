from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sentence_transformers import SentenceTransformer
import chromadb
from langdetect import detect
from deep_translator import GoogleTranslator

# Initialize FastAPI
app = FastAPI(
    title="Seva Setu API",
    description="Multilingual Search API for Indian Government Schemes — supports 9 Indian languages using cross-lingual transfer learning",
    version="1.0.0"
)

# Allow all origins for government portal integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Load model and database once at startup
print("Loading MuRIL model...")
model = SentenceTransformer('google/muril-base-cased')
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection("seva_setu_schemes")
print(f"Loaded {collection.count()} schemes")

# Language display names
LANGUAGE_NAMES = {
    'hi': 'Hindi', 'ta': 'Tamil', 'te': 'Telugu',
    'bn': 'Bengali', 'mr': 'Marathi', 'gu': 'Gujarati',
    'kn': 'Kannada', 'ml': 'Malayalam', 'en': 'English',
    'pa': 'Punjabi', 'it': 'English'
}

# Request model — what the API accepts
class SearchRequest(BaseModel):
    query: str
    n_results: Optional[int] = 5
    category: Optional[str] = None
    response_language: Optional[str] = None

# Response models — what the API returns
class SchemeResult(BaseModel):
    service_name: str
    ministry: str
    category: str
    portal_url: str
    relevance_score: float
    eligibility: str
    how_to_apply: str

class SearchResponse(BaseModel):
    query: str
    detected_language: str
    detected_language_name: str
    total_results: int
    results: list

# ── ENDPOINTS ──────────────────────────────────────

@app.get("/")
def home():
    return {
        "name": "Seva Setu API",
        "description": "Multilingual search for Indian government schemes",
        "version": "1.0.0",
        "supported_languages": [
            "Hindi", "Tamil", "Telugu", "Bengali",
            "Marathi", "Gujarati", "Kannada", "Malayalam", "English"
        ],
        "total_schemes": collection.count(),
        "endpoints": {
            "search": "POST /search",
            "health": "GET /health",
            "categories": "GET /categories",
            "docs": "GET /docs"
        }
    }

@app.post("/search")
def search(request: SearchRequest):
    # Validate query
    if not request.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")

    if len(request.query) > 500:
        raise HTTPException(status_code=400, detail="Query too long. Maximum 500 characters.")

    # Detect language
    SUPPORTED_LANGS = {'hi', 'ta', 'te', 'bn', 'mr', 'gu', 'kn', 'ml', 'en'}

    try:
        detected_lang = detect(request.query)
    except:
        detected_lang = 'unknown'

    if detected_lang not in SUPPORTED_LANGS:
        raise HTTPException(
            status_code=400,
            detail="Unsupported language. Please query in Hindi, Tamil, Telugu, Bengali, Marathi, Gujarati, Kannada, Malayalam, or English."
        )

    lang_name = LANGUAGE_NAMES.get(detected_lang, 'English')
    # Generate query embedding
    query_vector = model.encode(
        request.query,
        normalize_embeddings=True
    )

    # Build category filter
    where_filter = None
    if request.category and request.category != "All":
        where_filter = {"category": request.category}

    # Search ChromaDB
    n = min(request.n_results or 5, 10)
    results = collection.query(
        query_embeddings=[query_vector.tolist()],
        n_results=n,
        where=where_filter,
        include=['documents', 'metadatas', 'distances']
    )

    # Format results
    formatted_results = []
    for i in range(len(results['metadatas'][0])):
        meta = results['metadatas'][0][i]
        score = round(1 - results['distances'][0][i], 4)

        eligibility = meta.get('eligibility', '')
        how_to_apply = meta.get('how_to_apply', '')

        # Translate if needed
        target_lang = request.response_language or detected_lang
        if target_lang not in ['en', 'it']:
            try:
                eligibility = GoogleTranslator(
                    source='en', target=target_lang
                ).translate(eligibility)
                how_to_apply = GoogleTranslator(
                    source='en', target=target_lang
                ).translate(how_to_apply)
            except:
                pass  # fallback to English

        formatted_results.append({
            "service_name": meta.get('service_name', ''),
            "ministry": meta.get('ministry', ''),
            "category": meta.get('category', ''),
            "portal_url": meta.get('portal_url', ''),
            "relevance_score": score,
            "eligibility": eligibility,
            "how_to_apply": how_to_apply
        })

    return {
        "query": request.query,
        "detected_language": detected_lang,
        "detected_language_name": lang_name,
        "total_results": len(formatted_results),
        "results": formatted_results
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "schemes_indexed": collection.count(),
        "model": "google/muril-base-cased",
        "supported_languages": 9
    }

@app.get("/categories")
def get_categories():
    return {
        "categories": [
            "Agriculture", "Health", "Education",
            "Housing", "Employment", "Finance", "Identity"
        ]
    }

@app.get("/stats")
def get_stats():
    return {
        "total_schemes": collection.count(),
        "categories": 7,
        "languages_supported": 9,
        "model": "MuRIL — Multilingual Representations for Indian Languages",
        "embedding_dimensions": 768,
        "search_type": "Cross-lingual semantic search"
    }
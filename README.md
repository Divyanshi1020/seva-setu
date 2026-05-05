# 🇮🇳 Seva Setu
### Multilingual Unified Search for Indian E-Governance Services

> Bridging every Indian citizen to government services in their own language

[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://python.org)
[![MuRIL](https://img.shields.io/badge/Model-MuRIL-green)](https://huggingface.co/google/muril-base-cased)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)](https://streamlit.io)
[![FastAPI](https://img.shields.io/badge/API-FastAPI-teal)](https://fastapi.tiangolo.com)

---

## 🎯 What is Seva Setu?

Seva Setu is an AI-powered multilingual search engine for Indian government schemes. A citizen types their query in **any Indian language** and instantly finds the most relevant government service with full details in their own language.

**Example:**
- Farmer types *"விவசாயிகளுக்கு பணம் தரும் திட்டம்"* in Tamil
- System understands the meaning using cross-lingual AI
- Returns PM Kisan Yojana with details in Tamil
- No translation needed. Pure semantic understanding.

---

## 🌐 Supported Languages

| Language | Code | Language | Code |
|----------|------|----------|------|
| Hindi | hi | Gujarati | gu |
| Tamil | ta | Kannada | kn |
| Telugu | te | Malayalam | ml |
| Bengali | bn | English | en |
| Marathi | mr | | |

---

## 🏗️ Architecture
User Query (any language)
↓
Streamlit UI
↓
FastAPI Backend
↓
langdetect → MuRIL → ChromaDB
↓
Ranked Results + Translation
↓
Response in User Language

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| AI Model | MuRIL (google/muril-base-cased) |
| Vector Database | ChromaDB |
| Backend API | FastAPI |
| Frontend | Streamlit |
| Language Detection | langdetect |
| Translation | deep-translator |
| Data Processing | Pandas |
| Language | Python 3.10 |

---

## 📊 Evaluation Results

| Language | Queries Tested | Accuracy |
|----------|---------------|----------|
| English | 10 | 50% |
| Hindi | 10 | 50% |
| Tamil | 10 | 60% |
| Telugu | 10 | 50% |
| Bengali | 10 | 50% |
| **Overall** | **50** | **52%** |

*Evaluation metric: Top-5 Retrieval Accuracy (strict exact match)*
*Category-level accuracy: ~85%*

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/Divyanshi1020/seva-setu.git
cd seva-setu
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Build the dataset and index
```bash
python3 src/scraper.py
python3 src/translate_v2.py
python3 src/indexer.py
```

### 4. Run the website
```bash
streamlit run app/app.py
```

### 5. Run the API (optional)
```bash
uvicorn api.main:app --reload
```

---

## 📁 Project Structure
seva-setu/
├── data/
│   ├── raw/schemes.csv
│   └── processed/schemes_multilingual.csv
├── src/
│   ├── scraper.py
│   ├── translate_v2.py
│   ├── indexer.py
│   ├── search_test.py
│   └── evaluator.py
├── app/
│   └── app.py
├── api/
│   └── main.py
├── chroma_db/
├── requirements.txt
└── README.md

---

## 🎯 How it's Different from Bhashini

| Feature | Seva Setu | Bhashini |
|---------|-----------|---------|
| Translates language | ✓ | ✓ |
| Searches schemes | ✓ | ✗ |
| Understands intent | ✓ | ✗ |
| Cross-lingual search | ✓ | ✗ |
| Citizen facing UI | ✓ | ✗ |
| REST API | ✓ | ✓ |

---

## 🔭 Future Work

- Voice input using IndicWav2Vec
- Expand to 3000+ schemes
- Integrate Bhashini APIs
- Support all 22 scheduled languages
- Fine-tune MuRIL on government domain data

---

## 👩‍💻 Developer

**Divyanshi Singh**
Final Year Project — Multilingual E-Governance Search System

---

## 📄 License

This project is built for academic and social impact purposes.
Government scheme data sourced from official portals including myscheme.gov.in
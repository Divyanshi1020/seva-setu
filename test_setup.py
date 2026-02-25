print("Testing your setup...")
print("")

try:
    from sentence_transformers import SentenceTransformer
    print("✓ AI model library ready")
except:
    print("✗ sentence-transformers FAILED")

try:
    import chromadb
    print("✓ Vector database ready")
except:
    print("✗ chromadb FAILED")

try:
    import streamlit
    print("✓ Website builder ready")
except:
    print("✗ streamlit FAILED")

try:
    import fastapi
    print("✓ API framework ready")
except:
    print("✗ fastapi FAILED")

try:
    import pandas
    print("✓ Data library ready")
except:
    print("✗ pandas FAILED")

try:
    from langdetect import detect
    print("✓ Language detector ready")
except:
    print("✗ langdetect FAILED")

try:
    from deep_translator import GoogleTranslator
    print("✓ Translator ready")
except:
    print("✗ deep-translator FAILED")

print("")
print("All done!")
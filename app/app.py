import streamlit as st
import chromadb
from sentence_transformers import SentenceTransformer
from langdetect import detect
from deep_translator import GoogleTranslator
import sys
sys.path.append('../src')

# Page configuration
st.set_page_config(
    page_title="Seva Setu",
    page_icon="🇮🇳",
    layout="wide"
)

# Load model and database — cached so it loads only once
@st.cache_resource
def load_system():
    model = SentenceTransformer('google/muril-base-cased')
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_collection("seva_setu_schemes")
    return model, collection

model, collection = load_system()

# Language names for display
LANGUAGE_NAMES = {
    'hi': 'Hindi', 'ta': 'Tamil', 'te': 'Telugu',
    'bn': 'Bengali', 'mr': 'Marathi', 'gu': 'Gujarati',
    'kn': 'Kannada', 'ml': 'Malayalam', 'en': 'English',
    'pa': 'Punjabi', 'or': 'Odia', 'it': 'English'
}

def search(query, n_results=5, category=None):
    query_vector = model.encode(query, normalize_embeddings=True)
    
    where_filter = {"category": category} if category and category != "All" else None
    
    results = collection.query(
        query_embeddings=[query_vector.tolist()],
        n_results=n_results,
        where=where_filter
    )
    return results

def translate_to(text, lang_code):
    if lang_code in ['en', 'it']:
        return text
    try:
        return GoogleTranslator(source='en', target=lang_code).translate(text)
    except:
        return text

# ─── UI STARTS HERE ───────────────────────────────────────

# Header
st.markdown("""
    <div style='text-align: center; padding: 20px;'>
        <h1>🇮🇳 Seva Setu</h1>
        <h4>सरकारी सेवाएं खोजें | தேடுங்கள் | సేవలు వెతకండి | সরকারি সেবা খুঁজুন</h4>
        <p>Search Indian Government Services in Any Language</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# Sidebar filters
st.sidebar.header("🔧 Filters")
category = st.sidebar.selectbox(
    "Category",
    ["All", "Agriculture", "Health", "Education",
     "Housing", "Employment", "Finance", "Identity"]
)
n_results = st.sidebar.slider("Number of Results", 1, 10, 5)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🌐 Supported Languages")
st.sidebar.markdown("""
Hindi • Tamil • Telugu • Bengali  
Marathi • Gujarati • Kannada  
Malayalam • English
""")

st.sidebar.markdown("---")
st.sidebar.markdown("### ℹ️ About")
st.sidebar.markdown("""
Seva Setu uses **MuRIL** — Google's 
multilingual AI model trained on 
17 Indian languages — to understand 
your query in any language and find 
the most relevant government service.
""")

# Search bar
query = st.text_input(
    "🔍 Type your query in any language:",
    placeholder="e.g.  farmer scheme  |  राशन कार्ड  |  ரேஷன் கார்டு  |  স্বাস্থ্য বীমা"
)

# Example query buttons
st.markdown("**Try these examples:**")
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("🌾 PM Kisan"):
        query = "farmer income support scheme"
with col2:
    if st.button("🏥 आयुष्मान"):
        query = "गरीब परिवारों के लिए स्वास्थ्य बीमा"
with col3:
    if st.button("🏠 வீட்டு திட்டம்"):
        query = "வீடு கட்ட அரசு உதவி"
with col4:
    if st.button("📚 শিক্ষা"):
        query = "শিশুদের জন্য বিনামূল্যে শিক্ষা"
with col5:
    if st.button("💼 रोजगार"):
        query = "रोजगार के लिए सरकारी योजना"

# Search and display results
if query:
    with st.spinner("Searching across all government services..."):
        # Detect language
        try:
            detected_lang = detect(query)
        except:
            detected_lang = 'en'
        
        lang_name = LANGUAGE_NAMES.get(detected_lang, 'English')
        
        # Search
        results = search(query, n_results, category)
    
    # Results header
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    col1.metric("🌐 Detected Language", lang_name)
    col2.metric("📋 Results Found", len(results['metadatas'][0]))
    col3.metric("🎯 Top Relevance", f"{(1 - results['distances'][0][0]):.0%}")
    
    st.markdown("---")
    st.markdown("### Search Results")
    
    # Display each result as a card
    for i in range(len(results['metadatas'][0])):
        meta = results['metadatas'][0][i]
        score = 1 - results['distances'][0][i]
        
        with st.expander(
            f"**{i+1}. {meta['service_name']}**  "
            f"| {meta['category']}  "
            f"| Relevance: {score:.0%}",
            expanded=(i == 0)
        ):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"**Ministry:** {meta['ministry']}")
                st.markdown(f"**Category:** {meta['category']}")
                st.markdown(f"**Eligibility:** {meta['eligibility']}")
            
            with col2:
                st.markdown(f"**How to Apply:** {meta['how_to_apply']}")
                st.markdown(f"**Documents:** {meta['documents']}")
            
            st.markdown("---")
            
            # Translate details if query is not in English
            if detected_lang not in ['en', 'it']:
                with st.spinner(f"Translating to {lang_name}..."):
                    translated_eligibility = translate_to(
                        meta['eligibility'], detected_lang
                    )
                    translated_how = translate_to(
                        meta['how_to_apply'], detected_lang
                    )
                st.markdown(f"**{lang_name} — पात्रता / தகுதி / అర్హత:**")
                st.info(translated_eligibility)
                st.markdown(f"**{lang_name} — आवेदन / விண்ணப்பம் / దరఖాస్తు:**")
                st.info(translated_how)
            
            st.link_button(
                f"🔗 Apply / Visit Official Portal",
                meta['portal_url']
            )

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <p>Seva Setu — Bridging every Indian citizen to government services</p>
    <p>Powered by MuRIL (Google) | Built with ❤️ for Bharat</p>
</div>
""", unsafe_allow_html=True)
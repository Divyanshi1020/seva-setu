import streamlit as st
import chromadb
from sentence_transformers import SentenceTransformer
from langdetect import detect
from deep_translator import GoogleTranslator
import sys
sys.path.append('../src')

st.set_page_config(
    page_title="Seva Setu | सेवा सेतु",
    page_icon="🇮🇳",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,600;0,700;1,400&family=DM+Sans:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');

* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
.stApp { background: #F5F3EE !important; font-family: 'DM Sans', sans-serif; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* ── FORCE SIDEBAR ALWAYS OPEN ── */
section[data-testid="stSidebar"] {
    background: #ffffff !important;
    border-right: 1px solid #E0DDD6 !important;
    width: 270px !important;
    min-width: 270px !important;
    max-width: 270px !important;
    transform: none !important;
    display: flex !important;
    flex-direction: column !important;
}
section[data-testid="stSidebar"] > div:first-child {
    padding: 28px 22px !important;
    background: white !important;
    flex: 1 !important;
}
/* Hide the collapse arrow button */
button[data-testid="collapsedControl"] {
    display: none !important;
    visibility: hidden !important;
}
[data-testid="stSidebarCollapseButton"] {
    display: none !important;
    visibility: hidden !important;
}

/* ── SIDEBAR ELEMENTS ── */
section[data-testid="stSidebar"] .stRadio > label {
    font-size: 10px !important;
    letter-spacing: 1.5px !important;
    text-transform: uppercase !important;
    color: #999 !important;
    font-weight: 600 !important;
    margin-bottom: 8px !important;
}
section[data-testid="stSidebar"] .stRadio > div {
    gap: 2px !important;
}
section[data-testid="stSidebar"] .stRadio label {
    font-size: 13px !important;
    color: #444 !important;
    padding: 5px 8px !important;
    border-radius: 4px !important;
    font-family: 'DM Sans', sans-serif !important;
}
section[data-testid="stSidebar"] .stRadio label:hover {
    background: #F5F3EE !important;
}
section[data-testid="stSidebar"] .stSlider > label {
    font-size: 10px !important;
    letter-spacing: 1.5px !important;
    text-transform: uppercase !important;
    color: #999 !important;
    font-weight: 600 !important;
}

/* ── SEARCH INPUT ── */
.stTextInput input {
    font-family: 'DM Sans', sans-serif !important;
    font-size: 15px !important;
    border: 2px solid #1a3a5c !important;
    border-radius: 4px !important;
    padding: 12px 16px !important;
    background: white !important;
    color: #1a3a5c !important;
    box-shadow: none !important;
    width: 100% !important;
}
.stTextInput input:focus {
    border-color: #FF6B35 !important;
    box-shadow: 0 0 0 3px rgba(255,107,53,0.08) !important;
    outline: none !important;
}
.stTextInput input::placeholder { color: #bbb !important; }

/* ── BUTTONS ── */
.stButton > button {
    background: white !important;
    border: 1.5px solid #D0CAC0 !important;
    border-radius: 3px !important;
    color: #444 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 12px !important;
    padding: 6px 14px !important;
    font-weight: 400 !important;
    white-space: nowrap !important;
    transition: all 0.15s !important;
}
.stButton > button:hover {
    border-color: #1a3a5c !important;
    color: #1a3a5c !important;
    background: #F5F3EE !important;
}

/* ── EXPANDER ── */
.stExpander {
    border: 1px solid #E8E4DC !important;
    border-left: 4px solid #1a3a5c !important;
    border-radius: 4px !important;
    background: white !important;
    margin-bottom: 12px !important;
}
details > summary {
    font-family: 'EB Garamond', serif !important;
    font-size: 17px !important;
    color: #1a3a5c !important;
    font-weight: 600 !important;
    padding: 14px 16px !important;
}

/* ── INFO LABELS ── */
.info-label {
    font-size: 10px;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #999;
    margin-bottom: 4px;
    font-weight: 600;
    display: block;
}
.info-text {
    font-size: 13px;
    color: #333;
    line-height: 1.6;
    margin-bottom: 8px;
}
.info-translated {
    background: #EEF4FF;
    border-left: 3px solid #1a3a5c;
    padding: 8px 12px;
    border-radius: 3px;
    font-size: 13px;
    color: #1a3a5c;
    line-height: 1.6;
    margin-top: 4px;
}

/* ── LINK BUTTON ── */
.stLinkButton a {
    background: #1a3a5c !important;
    color: white !important;
    border: none !important;
    border-radius: 3px !important;
    padding: 8px 20px !important;
    font-size: 13px !important;
    font-family: 'DM Sans', sans-serif !important;
    text-decoration: none !important;
    display: inline-block !important;
}
.stLinkButton a:hover { background: #FF6B35 !important; }

hr {
    border: none !important;
    border-top: 1px solid #E8E4DC !important;
    margin: 16px 0 !important;
}
/* ── Responsive fixes ── */
.block-container {
    padding-left: 0 !important;
    padding-right: 0 !important;
    max-width: 100% !important;
}

div[data-testid="stMainBlockContainer"] {
    padding: 0 !important;
    max-width: 100% !important;
}

/* Main content area responsive padding */
@media screen and (max-width: 1024px) {
    section[data-testid="stSidebar"] {
        min-width: 220px !important;
        width: 220px !important;
    }
}

@media screen and (max-width: 768px) {
    section[data-testid="stSidebar"] {
        min-width: 180px !important;
        width: 180px !important;
    }
}

/* Prevent content collapse */
div[data-testid="stVerticalBlock"] {
    min-width: 0 !important;
    width: 100% !important;
}

/* Fix columns not wrapping */
div[data-testid="column"] {
    min-width: 0 !important;
    overflow: hidden !important;
}

/* Content padding responsive */
div[data-testid="stMainBlockContainer"] > div {
    padding: 20px 24px !important;
}
</style>
""", unsafe_allow_html=True)

# ── Load System ─────────────────────────────────────────
@st.cache_resource
def load_system():
    model = SentenceTransformer('google/muril-base-cased')
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_collection("seva_setu_schemes")
    return model, collection

model, collection = load_system()

LANGUAGE_NAMES = {
    'hi': 'Hindi', 'ta': 'Tamil', 'te': 'Telugu',
    'bn': 'Bengali', 'mr': 'Marathi', 'gu': 'Gujarati',
    'kn': 'Kannada', 'ml': 'Malayalam', 'en': 'English',
    'pa': 'Punjabi', 'or': 'Odia', 'it': 'English', 'sa': 'Sanskrit'
}

def search_schemes(query, n_results=5, category=None):
    query_vector = model.encode(query, normalize_embeddings=True)
    where_filter = {"category": category} if category and category != "All" else None
    results = collection.query(
        query_embeddings=[query_vector.tolist()],
        n_results=n_results,
        where=where_filter,
        include=['documents', 'metadatas', 'distances']
    )
    return results

def translate_to(text, lang_code):
    if lang_code in ['en', 'it', 'sa']:
        return None
    try:
        return GoogleTranslator(source='en', target=lang_code).translate(text)
    except:
        return None

# ══════════════════════════════════════════════════════════
# SIDEBAR — PERMANENT
# ══════════════════════════════════════════════════════════
with st.sidebar:

    #st.markdown("""
    #<div style="font-family:'EB Garamond',serif;#font-size:20px;
    #font-weight:700;color:#1a3a5c;margin-bottom:4px;">
    #Search Filters
    #</div>
    #<div style="height:1px;background:#E8E4DC;margin:12px 0 20px;"></div>
    #""", unsafe_allow_html=True)

    #category = st.radio(
        #"CATEGORY",
        #options=["All", "Agriculture", "Health", "Education",
               # "Housing", "Employment", "Finance", "Identity"]
    #)
    category ="All"

    st.markdown('<div style="height:1px;background:#E8E4DC;margin:16px 0;"></div>',
                unsafe_allow_html=True)

    n_results = st.slider("NUMBER OF RESULTS", min_value=1, max_value=10, value=5)

    st.markdown('<div style="height:1px;background:#E8E4DC;margin:16px 0; margin-top:0px;"></div>',
                unsafe_allow_html=True)

    st.markdown("""
    <div style="font-size:10px;letter-spacing:1.5px;text-transform:uppercase;
    color:#999;font-weight:600;margin-bottom:12px;">Supported Languages</div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:5px;
    margin-bottom:20px;">
        <div style="font-size:11px;color:#444;padding:4px 8px;
        background:#F5F3EE;border-radius:3px;">Hindi</div>
        <div style="font-size:11px;color:#444;padding:4px 8px;
        background:#F5F3EE;border-radius:3px;">Tamil</div>
        <div style="font-size:11px;color:#444;padding:4px 8px;
        background:#F5F3EE;border-radius:3px;">Telugu</div>
        <div style="font-size:11px;color:#444;padding:4px 8px;
        background:#F5F3EE;border-radius:3px;">Bengali</div>
        <div style="font-size:11px;color:#444;padding:4px 8px;
        background:#F5F3EE;border-radius:3px;">Marathi</div>
        <div style="font-size:11px;color:#444;padding:4px 8px;
        background:#F5F3EE;border-radius:3px;">Gujarati</div>
        <div style="font-size:11px;color:#444;padding:4px 8px;
        background:#F5F3EE;border-radius:3px;">Kannada</div>
        <div style="font-size:11px;color:#444;padding:4px 8px;
        background:#F5F3EE;border-radius:3px;">Malayalam</div>
        <div style="font-size:11px;color:#444;padding:4px 8px;
        background:#F5F3EE;border-radius:3px;grid-column:span 2;">
        English</div>
    </div>

    <div style="height:1px;background:#E8E4DC;margin:4px 0 16px;"></div>

    <div style="font-size:10px;letter-spacing:1.5px;text-transform:uppercase;
    color:#999;font-weight:600;margin-bottom:10px;">About</div>
    <div style="font-size:11px;color:#666;line-height:1.7;">
    Powered by <strong style="color:#1a3a5c;">MuRIL</strong> - Google's
    multilingual AI model trained on 17 Indian languages using
    <strong style="color:#1a3a5c;">Cross-Lingual Transfer Learning.</strong>
    <br><br>
    Data from <strong style="color:#1a3a5c;">myscheme.gov.in</strong>
    and official government portals.
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════
# MAIN CONTENT
# ══════════════════════════════════════════════════════════

# Gov Bar
st.markdown("""
<div style="background:#1a3a5c;color:white;padding:9px 40px;
font-size:12px;display:flex;align-items:center;gap:14px;
font-family:'DM Sans',sans-serif;letter-spacing:0.4px;">
    <span style="font-size:16px;"></span>
    <span style="opacity:0.85;">Government of India - Digital India Initiative</span>
    <span style="margin-left:auto;opacity:0.55;font-size:11px;">
    Powered by MuRIL · Cross-Lingual AI · Built for Bharat</span>
</div>
""", unsafe_allow_html=True)

# Header
st.markdown(f"""
<div style="background:white;border-bottom:3px solid #FF6B35;
padding:20px 40px;display:flex;align-items:center;gap:18px;">
    <div style="font-size:40px;line-height:1;flex-shrink:0;">🏛️</div>
    <div style="flex:1;">
        <div style="font-family:'EB Garamond',serif;font-size:30px;
        font-weight:700;color:#1a3a5c;line-height:1.1;">
            Seva <span style="color:#FF6B35;">Setu</span>
            <span style="font-size:15px;color:#bbb;font-weight:400;">
            &nbsp;/ सेवा सेतु</span>
        </div>
        <div style="font-size:12px;color:#666;margin-top:5px;">
        Multilingual Unified Search for Indian E-Governance Services</div>
        <div style="font-size:11px;color:#1a3a5c;margin-top:3px;opacity:0.7;">
        हिंदी · தமிழ் · తెలుగు · বাংলা · मराठी · ગુજરાતી · ಕನ್ನಡ · മലയാളം · English
        </div>
    </div>
    <div style="text-align:right;flex-shrink:0;">
        <div style="font-family:'EB Garamond',serif;font-size:32px;
        font-weight:700;color:#FF6B35;line-height:1;">{collection.count()}</div>
        <div style="font-size:9px;color:#999;letter-spacing:1px;
        text-transform:uppercase;margin-top:2px;">Schemes Indexed</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Content with proper margins
st.markdown('<div style="padding:32px 40px;">', unsafe_allow_html=True)

# Search hint
st.markdown("""
<div style="font-family:'EB Garamond',serif;font-size:16px;color:#555;
margin-bottom:10px;">Search for any government scheme in your language</div>
""", unsafe_allow_html=True)

# Search bar
if "search_query" not in st.session_state:
    st.session_state.search_query = ""

query = st.text_input(
    "query",
    placeholder="e.g.  farmer scheme  ·  राशन कार्ड  ·  ரேஷன் கார்டு  ·  வாஸ்த்ய பீமா  ·  ఆవాస్ యోజన",
    label_visibility="collapsed",
    key="search_query"
)

# Example buttons
st.markdown("""
<div style="font-size:10px;letter-spacing:1.5px;text-transform:uppercase;
color:#bbb;margin:14px 0 8px;font-weight:600;">Try an example</div>
""", unsafe_allow_html=True)

bc1, bc2, bc3, bc4, bc5, bc6 = st.columns([1, 1, 1.3, 1, 1, 3])
with bc1:
    if st.button("PM Kisan"):
        st.session_state.search_query = "farmer income support scheme"
        st.rerun()
with bc2:
    if st.button("आयुष्मान"):
        st.session_state.search_query = "गरीब परिवारों के लिए स्वास्थ्य बीमा"
        st.rerun()
with bc3:
    if st.button("வீட்டு திட்டம்"):
        st.session_state.search_query = "வீடு கட்ட அரசு உதவி"
        st.rerun()
with bc4:
    if st.button("বৃত্তি"):
        st.session_state.search_query = "ছাত্রদের জন্য বৃত্তি"
        st.rerun()
with bc5:
    if st.button("ఉపాధి"):
        st.session_state.search_query = "యువతకు నైపుణ్య శిక్షణ"
        st.rerun()

st.markdown('<div style="height:1px;background:#E8E4DC;margin:20px 0;"></div>',
            unsafe_allow_html=True)

# Results
if query:
    import unicodedata

    INDIAN_SCRIPTS = {'Devanagari', 'Tamil', 'Telugu', 'Bengali', 'Gujarati', 'Kannada', 'Malayalam'}

    def get_script_type(text):
        found = set()
        for ch in text:
            if ch.isspace() or not ch.isalpha():
                continue
            name = unicodedata.name(ch, '')
            word = name.split(' ')[0].capitalize()
            if word in INDIAN_SCRIPTS:
                found.add('indian')
            elif word == 'Latin':
                found.add('latin')
            else:
                return 'invalid'
        if not found:
            return 'invalid'
        if len(found) > 1:
            return 'invalid'
        return found.pop()

    script = get_script_type(query)

    if script == 'invalid':
        st.error("Invalid query. Please type in Hindi, Tamil, Telugu, Bengali, Marathi, Gujarati, Kannada, Malayalam, or English.")
        st.stop()

    if script == 'latin':
        detected_lang = 'en'
    else:
        try:
            detected_lang = detect(query)
        except:
            detected_lang = 'hi'
        if detected_lang not in {'hi', 'ta', 'te', 'bn', 'mr', 'gu', 'kn', 'ml'}:
            detected_lang = 'hi'

    with st.spinner("Searching across all government schemes..."):
        lang_name = LANGUAGE_NAMES.get(detected_lang, 'English')
        results = search_schemes(query, n_results, category)

    st.markdown(f"""
    <div style="font-family:'EB Garamond',serif;font-size:13px;
    color:#999;margin-bottom:16px;">
    Showing <strong style="color:#1a3a5c;">
    {len(results['metadatas'][0])}</strong> results for
    <em>"{query[:50]}{'...' if len(query)>50 else ''}"</em>
    &nbsp;·&nbsp; Language:
    <strong style="color:#1a3a5c;">{lang_name}</strong>
    </div>
    """, unsafe_allow_html=True)

    for i in range(len(results['metadatas'][0])):
        meta = results['metadatas'][0][i]
        score = round((1 - results['distances'][0][i]) * 100)
        is_top = i == 0
        label = (f"{'★  ' if is_top else ''}"
                 f"{meta['service_name']}  ·  "
                 f"{meta['category']}  ·  {score}%")

        with st.expander(label, expanded=(i == 0)):
            col1, col2 = st.columns(2)

            with col1:
                st.markdown(f"""
                <span class="info-label">Ministry</span>
                <div class="info-text">{meta['ministry']}</div>
                <span class="info-label">Category</span>
                <div class="info-text">
                <span style="background:#E8F0FE;color:#1a3a5c;
                padding:3px 10px;border-radius:2px;font-size:12px;
                font-weight:500;">{meta['category']}</span>
                </div>
                <span class="info-label">Relevance Score</span>
                <div class="info-text">
                <span style="font-family:'JetBrains Mono',monospace;
                color:#FF6B35;font-weight:600;font-size:15px;">
                {score}%</span>
                </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown(f"""
                <span class="info-label">Eligibility</span>
                <div class="info-text">{meta['eligibility']}</div>
                <span class="info-label">How to Apply</span>
                <div class="info-text">{meta['how_to_apply']}</div>
                """, unsafe_allow_html=True)

            # Translation
            if detected_lang not in ['en', 'it']:
                st.markdown(f"""
                <div style="height:1px;background:#E8E4DC;margin:16px 0;"></div>
                <div style="font-size:10px;letter-spacing:1.5px;
                text-transform:uppercase;color:#1a3a5c;
                font-weight:600;margin-bottom:10px;">
                ● {lang_name} Translation</div>
                """, unsafe_allow_html=True)

                with st.spinner(f"Translating to {lang_name}..."):
                    t_e = translate_to(meta['eligibility'], detected_lang)
                    t_a = translate_to(meta['how_to_apply'], detected_lang)

                tr1, tr2 = st.columns(2)
                with tr1:
                    if t_e:
                        st.markdown(f"""
                        <span class="info-label">
                        Eligibility — {lang_name}</span>
                        <div class="info-translated">{t_e}</div>
                        """, unsafe_allow_html=True)
                with tr2:
                    if t_a:
                        st.markdown(f"""
                        <span class="info-label">
                        How to Apply — {lang_name}</span>
                        <div class="info-translated">{t_a}</div>
                        """, unsafe_allow_html=True)

            st.markdown("<div style='margin-top:16px;'>",
                        unsafe_allow_html=True)
            st.link_button("→ Apply / Visit Official Portal",
                           meta['portal_url'])
            st.markdown("</div>", unsafe_allow_html=True)

else:
    st.markdown("""
    <div style="text-align:center;padding:80px 20px;">
        <div style="font-size:36px;margin-bottom:16px;opacity:0.12;">🔍</div>
        <div style="font-family:'EB Garamond',serif;font-size:22px;
        color:#bbb;margin-bottom:8px;">Enter a query to begin</div>
        <div style="font-size:13px;color:#ccc;max-width:420px;
        margin:0 auto;line-height:1.7;">
        Type in any Indian language — Hindi, Tamil, Telugu, Bengali,
        Marathi, Gujarati, Kannada, or Malayalam
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="background:#1a3a5c;color:rgba(255,255,255,0.5);
padding:16px 40px;font-size:11px;display:flex;
justify-content:space-between;align-items:center;
margin-top:40px;font-family:'DM Sans',sans-serif;">
    <div style="font-family:'EB Garamond',serif;font-size:14px;
    color:rgba(255,255,255,0.85);">Seva Setu · सेवा सेतु</div>
    <div>MuRIL · ChromaDB · FastAPI · Streamlit ·
    Cross-Lingual Transfer Learning · Final Year Project</div>
</div>
""", unsafe_allow_html=True)
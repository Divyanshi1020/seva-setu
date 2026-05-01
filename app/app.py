import streamlit as st
import chromadb
from sentence_transformers import SentenceTransformer
from langdetect import detect
from deep_translator import GoogleTranslator
import sys
sys.path.append('../src')

# ─── PAGE CONFIG ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Seva Setu — Government Services Search",
    page_icon="🇮🇳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── STYLING ──────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap');

/* ── Reset & Base ── */
*, *::before, *::after { box-sizing: border-box; }

html, body, [class*="css"] {
    font-family: 'IBM Plex Sans', sans-serif;
    color: #1a1a2e;
}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
section[data-testid="stSidebar"] > div { padding-top: 0 !important; }

/* ── Color tokens ── */
:root {
    --navy:        #0f2044;
    --navy-mid:    #1a3560;
    --saffron:     #FF6B00;
    --saffron-lt:  #FF8C38;
    --green:       #138808;
    --green-lt:    #1aab0a;
    --white:       #ffffff;
    --off-white:   #f7f8fc;
    --border:      #dde2ee;
    --text-main:   #1a1a2e;
    --text-muted:  #5a6a8a;
    --card-bg:     #ffffff;
    --shadow:      0 2px 16px rgba(15,32,68,0.10);
    --shadow-lg:   0 8px 32px rgba(15,32,68,0.14);
}

/* ── Sidebar ── */
section[data-testid="stSidebar"] {
    background: var(--navy) !important;
    border-right: none;
}
section[data-testid="stSidebar"] * {
    color: rgba(255,255,255,0.9) !important;
}
section[data-testid="stSidebar"] .stSelectbox label,
section[data-testid="stSidebar"] .stSlider label {
    color: rgba(255,255,255,0.65) !important;
    font-size: 11px !important;
    letter-spacing: 0.08em !important;
    text-transform: uppercase !important;
    font-weight: 600 !important;
}
section[data-testid="stSidebar"] .stSelectbox > div > div {
    background: rgba(255,255,255,0.08) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    color: white !important;
    border-radius: 6px !important;
}
section[data-testid="stSidebar"] hr {
    border-color: rgba(255,255,255,0.12) !important;
}

/* ── Top header bar ── */
.seva-topbar {
    background: var(--navy);
    padding: 0 40px;
    height: 56px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 3px solid var(--saffron);
}
.seva-topbar-left {
    display: flex;
    align-items: center;
    gap: 14px;
}
.seva-emblem {
    font-size: 28px;
    line-height: 1;
}
.seva-brand {
    display: flex;
    flex-direction: column;
    gap: 1px;
}
.seva-brand-name {
    font-size: 18px;
    font-weight: 700;
    color: white;
    letter-spacing: 0.02em;
    line-height: 1;
}
.seva-brand-tagline {
    font-size: 10px;
    color: rgba(255,255,255,0.55);
    letter-spacing: 0.12em;
    text-transform: uppercase;
    font-weight: 500;
}
.seva-topbar-right {
    display: flex;
    align-items: center;
    gap: 8px;
}
.seva-lang-pill {
    background: rgba(255,107,0,0.18);
    border: 1px solid rgba(255,107,0,0.4);
    color: #FF8C38;
    font-size: 10px;
    font-weight: 600;
    padding: 3px 8px;
    border-radius: 20px;
    letter-spacing: 0.06em;
    font-family: 'IBM Plex Mono', monospace;
}

/* ── Tricolor accent bar ── */
.tricolor-bar {
    height: 4px;
    background: linear-gradient(to right,
        #FF6B00 0%, #FF6B00 33.3%,
        #ffffff 33.3%, #ffffff 66.6%,
        #138808 66.6%, #138808 100%
    );
    margin-bottom: 0;
}

/* ── Hero section ── */
.seva-hero {
    background: var(--off-white);
    padding: 40px 40px 32px;
    border-bottom: 1px solid var(--border);
}
.seva-hero-title {
    font-size: 28px;
    font-weight: 700;
    color: var(--navy);
    margin: 0 0 6px 0;
    line-height: 1.2;
}
.seva-hero-sub {
    font-size: 14px;
    color: var(--text-muted);
    margin: 0 0 24px 0;
    font-weight: 400;
}
.seva-hero-langs {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 28px;
}
.seva-hero-lang-chip {
    background: white;
    border: 1px solid var(--border);
    color: var(--navy-mid);
    font-size: 12px;
    font-weight: 500;
    padding: 4px 12px;
    border-radius: 4px;
    letter-spacing: 0.02em;
}

/* ── Search box ── */
.stTextInput > div > div > input {
    font-family: 'IBM Plex Sans', sans-serif !important;
    font-size: 16px !important;
    font-weight: 400 !important;
    color: var(--text-main) !important;
    background: white !important;
    border: 2px solid var(--border) !important;
    border-radius: 8px !important;
    padding: 14px 18px !important;
    height: 54px !important;
    transition: border-color 0.2s !important;
    box-shadow: var(--shadow) !important;
}
.stTextInput > div > div > input:focus {
    border-color: var(--navy) !important;
    box-shadow: 0 0 0 3px rgba(15,32,68,0.08) !important;
}
.stTextInput label {
    font-size: 11px !important;
    font-weight: 600 !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
    color: var(--text-muted) !important;
    margin-bottom: 6px !important;
}

/* ── Quick example buttons ── */
.stButton > button {
    font-family: 'IBM Plex Sans', sans-serif !important;
    font-size: 12px !important;
    font-weight: 500 !important;
    background: white !important;
    color: var(--navy-mid) !important;
    border: 1px solid var(--border) !important;
    border-radius: 6px !important;
    padding: 7px 14px !important;
    transition: all 0.15s !important;
    white-space: nowrap !important;
}
.stButton > button:hover {
    background: var(--navy) !important;
    color: white !important;
    border-color: var(--navy) !important;
    transform: translateY(-1px) !important;
    box-shadow: var(--shadow) !important;
}

/* ── Metric cards ── */
[data-testid="metric-container"] {
    background: white;
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 16px 20px !important;
    box-shadow: var(--shadow);
}
[data-testid="metric-container"] label {
    font-size: 10px !important;
    font-weight: 600 !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
    color: var(--text-muted) !important;
}
[data-testid="metric-container"] [data-testid="stMetricValue"] {
    font-size: 22px !important;
    font-weight: 700 !important;
    color: var(--navy) !important;
}

/* ── Result cards ── */
.result-card {
    background: white;
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 22px 26px;
    margin-bottom: 14px;
    box-shadow: var(--shadow);
    transition: box-shadow 0.2s, border-color 0.2s;
    position: relative;
    overflow: hidden;
}
.result-card:hover {
    box-shadow: var(--shadow-lg);
    border-color: #c8d0e4;
}
.result-card-rank {
    position: absolute;
    top: 0;
    left: 0;
    width: 4px;
    height: 100%;
    background: var(--navy);
    border-radius: 10px 0 0 10px;
}
.result-card-rank.top {
    background: var(--saffron);
}
.result-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 12px;
    gap: 12px;
}
.result-name {
    font-size: 16px;
    font-weight: 700;
    color: var(--navy);
    line-height: 1.3;
}
.result-score-badge {
    background: var(--navy);
    color: white;
    font-size: 11px;
    font-weight: 600;
    padding: 4px 10px;
    border-radius: 20px;
    white-space: nowrap;
    font-family: 'IBM Plex Mono', monospace;
    flex-shrink: 0;
}
.result-score-badge.high {
    background: var(--green);
}
.result-score-badge.medium {
    background: var(--navy-mid);
}
.result-meta {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 14px;
}
.result-meta-chip {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    background: var(--off-white);
    border: 1px solid var(--border);
    color: var(--text-muted);
    font-size: 11px;
    font-weight: 500;
    padding: 4px 10px;
    border-radius: 4px;
}
.result-section-label {
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--text-muted);
    margin-bottom: 4px;
    margin-top: 12px;
}
.result-section-text {
    font-size: 13px;
    color: var(--text-main);
    line-height: 1.6;
}
.result-translated {
    background: #fff9f5;
    border: 1px solid #ffd4b0;
    border-radius: 6px;
    padding: 12px 14px;
    margin-top: 8px;
}
.result-translated-label {
    font-size: 10px;
    font-weight: 600;
    color: var(--saffron);
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 4px;
}
.result-translated-text {
    font-size: 13px;
    color: #5a3010;
    line-height: 1.6;
}
.result-apply-btn {
    display: inline-block;
    background: var(--navy);
    color: white !important;
    font-size: 12px;
    font-weight: 600;
    padding: 10px 20px;
    border-radius: 6px;
    text-decoration: none;
    margin-top: 16px;
    letter-spacing: 0.04em;
    transition: background 0.15s;
}
.result-apply-btn:hover {
    background: var(--navy-mid);
}

/* ── Section heading ── */
.section-heading {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--text-muted);
    margin: 28px 0 16px;
    display: flex;
    align-items: center;
    gap: 10px;
}
.section-heading::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--border);
}

/* ── Info banner ── */
.info-banner {
    background: #eef2ff;
    border: 1px solid #c7d2fe;
    border-radius: 8px;
    padding: 12px 16px;
    font-size: 13px;
    color: #3730a3;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 10px;
}

/* ── Footer ── */
.seva-footer {
    background: var(--navy);
    color: rgba(255,255,255,0.45);
    font-size: 11px;
    text-align: center;
    padding: 18px 40px;
    margin-top: 40px;
    letter-spacing: 0.04em;
}
.seva-footer strong {
    color: rgba(255,255,255,0.7);
}

/* ── Spinner override ── */
.stSpinner > div {
    border-top-color: var(--saffron) !important;
}

/* ── Expander override ── */
.streamlit-expanderHeader {
    font-family: 'IBM Plex Sans', sans-serif !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    color: var(--navy) !important;
    background: white !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
}

/* ── Main content padding ── */
.main-content {
    padding: 0 40px 40px;
    max-width: 1200px;
}

/* ── Divider ── */
.seva-divider {
    border: none;
    border-top: 1px solid var(--border);
    margin: 24px 0;
}
</style>
""", unsafe_allow_html=True)

# ─── LOAD MODEL & DB ──────────────────────────────────────────────────────────
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
    'pa': 'Punjabi', 'or': 'Odia', 'ur': 'Urdu',
    'it': 'English', 'af': 'English', 'sq': 'English'
}

CATEGORY_ICONS = {
    'Agriculture': '🌾',
    'Health': '🏥',
    'Education': '📚',
    'Housing': '🏠',
    'Employment': '💼',
    'Finance': '💰',
    'Identity': '🪪',
    'All': '🔍'
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
    if lang_code in ['en', 'it', 'af', 'sq']:
        return None
    try:
        return GoogleTranslator(source='en', target=lang_code).translate(text)
    except:
        return None

def get_score_class(score):
    if score >= 0.80:
        return "high"
    return "medium"

# ─── TOP BAR ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="seva-topbar">
    <div class="seva-topbar-left">
        <div class="seva-emblem">🇮🇳</div>
        <div class="seva-brand">
            <div class="seva-brand-name">Seva Setu</div>
            <div class="seva-brand-tagline">Government Services Discovery Platform</div>
        </div>
    </div>
    <div class="seva-topbar-right">
        <span class="seva-lang-pill">HI</span>
        <span class="seva-lang-pill">TA</span>
        <span class="seva-lang-pill">TE</span>
        <span class="seva-lang-pill">BN</span>
        <span class="seva-lang-pill">MR</span>
        <span class="seva-lang-pill">+4</span>
    </div>
</div>
<div class="tricolor-bar"></div>
""", unsafe_allow_html=True)

# ─── SIDEBAR ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("<div style='padding: 24px 20px 0;'>", unsafe_allow_html=True)
    st.markdown("""
    <div style='font-size:10px; font-weight:700; letter-spacing:0.14em;
                text-transform:uppercase; color:rgba(255,255,255,0.4);
                margin-bottom:20px;'>
        Search Filters
    </div>
    """, unsafe_allow_html=True)

    category = st.selectbox(
        "Category",
        ["All", "Agriculture", "Health", "Education",
         "Housing", "Employment", "Finance", "Identity"],
        format_func=lambda x: f"{CATEGORY_ICONS.get(x,'')}  {x}"
    )

    n_results = st.slider("Results to show", 1, 10, 5)

    st.markdown("<hr style='margin:24px 0;'>", unsafe_allow_html=True)

    st.markdown("""
    <div style='font-size:10px; font-weight:700; letter-spacing:0.14em;
                text-transform:uppercase; color:rgba(255,255,255,0.4);
                margin-bottom:14px;'>
        Supported Languages
    </div>
    <div style='font-size:12px; color:rgba(255,255,255,0.65); line-height:2;'>
        Hindi &nbsp;·&nbsp; Tamil &nbsp;·&nbsp; Telugu<br>
        Bengali &nbsp;·&nbsp; Marathi &nbsp;·&nbsp; Gujarati<br>
        Kannada &nbsp;·&nbsp; Malayalam &nbsp;·&nbsp; English
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='margin:24px 0;'>", unsafe_allow_html=True)

    st.markdown("""
    <div style='font-size:10px; font-weight:700; letter-spacing:0.14em;
                text-transform:uppercase; color:rgba(255,255,255,0.4);
                margin-bottom:10px;'>
        Powered By
    </div>
    <div style='font-size:11px; color:rgba(255,255,255,0.5); line-height:1.9;'>
        MuRIL · Google<br>
        Cross-Lingual Transfer Learning<br>
        ChromaDB · Vector Search<br>
        FastAPI · Streamlit
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ─── HERO & SEARCH ────────────────────────────────────────────────────────────
st.markdown("""
<div class="seva-hero">
    <h1 class="seva-hero-title">Find the right government service,<br>in your language.</h1>
    <p class="seva-hero-sub">Search across 95+ central government schemes instantly — type in any Indian language.</p>
    <div class="seva-hero-langs">
        <span class="seva-hero-lang-chip">हिन्दी</span>
        <span class="seva-hero-lang-chip">தமிழ்</span>
        <span class="seva-hero-lang-chip">తెలుగు</span>
        <span class="seva-hero-lang-chip">বাংলা</span>
        <span class="seva-hero-lang-chip">मराठी</span>
        <span class="seva-hero-lang-chip">ગુજરાતી</span>
        <span class="seva-hero-lang-chip">ಕನ್ನಡ</span>
        <span class="seva-hero-lang-chip">മലയാളം</span>
        <span class="seva-hero-lang-chip">English</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Search input + example buttons in the hero padding
st.markdown("<div style='padding: 28px 40px 0;'>", unsafe_allow_html=True)

query = st.text_input(
    "SEARCH QUERY",
    placeholder="e.g.  farmer income support  ·  राशन कार्ड  ·  ரேஷன் கார்டு  ·  স্বাস্থ্য বীমা"
)

st.markdown("<div style='font-size:11px; font-weight:600; letter-spacing:0.09em; text-transform:uppercase; color:#5a6a8a; margin:14px 0 10px;'>Try an example</div>", unsafe_allow_html=True)

col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    if st.button("🌾 PM Kisan"):
        query = "farmer income support money"
with col2:
    if st.button("🏥 आयुष्मान"):
        query = "गरीब परिवारों के लिए स्वास्थ्य बीमा"
with col3:
    if st.button("🏠 வீட்டு திட்டம்"):
        query = "வீடு கட்ட அரசு உதவி"
with col4:
    if st.button("📚 শিক্ষাবৃত্তি"):
        query = "শিক্ষার জন্য বৃত্তি"
with col5:
    if st.button("💼 रोजगार"):
        query = "रोजगार के लिए सरकारी योजना"
with col6:
    if st.button("🪪 Aadhaar"):
        query = "Aadhaar card enrollment update"

st.markdown("</div>", unsafe_allow_html=True)

# ─── RESULTS ──────────────────────────────────────────────────────────────────
if query and query.strip():
    st.markdown("<div style='padding: 0 40px;'>", unsafe_allow_html=True)

    with st.spinner("Searching across government schemes..."):
        try:
            detected_lang = detect(query)
        except:
            detected_lang = 'en'
        lang_name = LANGUAGE_NAMES.get(detected_lang, 'English')
        cat_filter = None if category == "All" else category
        results = search(query, n_results, cat_filter)

    num_found = len(results['metadatas'][0])

    # ── Metrics row ──
    st.markdown("<div style='height:24px;'></div>", unsafe_allow_html=True)
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Detected Language", lang_name)
    m2.metric("Schemes Found", num_found)
    if num_found > 0:
        top_score = (1 - results['distances'][0][0])
        m3.metric("Top Match", f"{top_score:.0%}")
        m4.metric("Category Filter", category)

    # ── Section heading ──
    st.markdown(f"""
    <div class="section-heading" style='margin-top:28px;'>
        Search Results
    </div>
    """, unsafe_allow_html=True)

    if num_found == 0:
        st.markdown("""
        <div class="info-banner">
            ℹ️ No schemes found for this query. Try different keywords or remove the category filter.
        </div>
        """, unsafe_allow_html=True)
    else:
        for i in range(num_found):
            meta = results['metadatas'][0][i]
            score = 1 - results['distances'][0][i]
            score_class = get_score_class(score)
            rank_class = "top" if i == 0 else ""
            cat_icon = CATEGORY_ICONS.get(meta.get('category', ''), '📋')

            # Translate if non-English
            translated_eligibility = None
            translated_how = None
            if detected_lang not in ['en', 'it', 'af', 'sq']:
                translated_eligibility = translate_to(meta.get('eligibility', ''), detected_lang)
                translated_how = translate_to(meta.get('how_to_apply', ''), detected_lang)

            eligibility_display = meta.get('eligibility', 'N/A')
            how_display = meta.get('how_to_apply', 'N/A')

            # Build translated blocks HTML
            trans_elig_html = ""
            if translated_eligibility:
                trans_elig_html = f"""
                <div class="result-translated" style="margin-top:6px;">
                    <div class="result-translated-label">🌐 {lang_name}</div>
                    <div class="result-translated-text">{translated_eligibility}</div>
                </div>"""

            trans_how_html = ""
            if translated_how:
                trans_how_html = f"""
                <div class="result-translated" style="margin-top:6px;">
                    <div class="result-translated-label">🌐 {lang_name}</div>
                    <div class="result-translated-text">{translated_how}</div>
                </div>"""

            st.markdown(f"""
            <div class="result-card">
                <div class="result-card-rank {rank_class}"></div>
                <div style="padding-left: 12px;">
                    <div class="result-header">
                        <div class="result-name">{i+1}. {meta.get('service_name', 'Unknown')}</div>
                        <span class="result-score-badge {score_class}">{score:.0%} match</span>
                    </div>
                    <div class="result-meta">
                        <span class="result-meta-chip">{cat_icon} {meta.get('category','—')}</span>
                        <span class="result-meta-chip">🏛️ {meta.get('ministry','—')}</span>
                    </div>
                    <div class="result-section-label">Eligibility</div>
                    <div class="result-section-text">{eligibility_display}</div>
                    {trans_elig_html}
                    <div class="result-section-label">How to Apply</div>
                    <div class="result-section-text">{how_display}</div>
                    {trans_how_html}
                    <a class="result-apply-btn" href="{meta.get('portal_url','#')}" target="_blank">
                        Visit Official Portal →
                    </a>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

else:
    # Empty state
    st.markdown("""
    <div style='padding: 60px 40px; text-align: center;'>
        <div style='font-size: 48px; margin-bottom: 16px;'>🔍</div>
        <div style='font-size: 18px; font-weight: 600; color: #1a1a2e; margin-bottom: 8px;'>
            Search in your language
        </div>
        <div style='font-size: 14px; color: #5a6a8a; max-width: 480px; margin: 0 auto; line-height: 1.7;'>
            Type your query above in Hindi, Tamil, Telugu, Bengali, or any other Indian language.
            Seva Setu understands the meaning — not just the words.
        </div>
    </div>
    """, unsafe_allow_html=True)

# ─── FOOTER ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="seva-footer">
    <strong>Seva Setu</strong> &nbsp;·&nbsp;
    Powered by <strong>MuRIL</strong> (Google) &nbsp;·&nbsp;
    Cross-Lingual Transfer Learning &nbsp;·&nbsp;
    95+ Government Schemes &nbsp;·&nbsp;
    9 Indian Languages
</div>
""", unsafe_allow_html=True)
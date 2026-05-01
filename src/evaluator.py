import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sentence_transformers import SentenceTransformer
import chromadb
from langdetect import detect

print("Seva Setu — Evaluation Script")
print("=" * 50)

# Load model and database
model = SentenceTransformer('google/muril-base-cased')
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection("seva_setu_schemes")

def search(query, n_results=5):
    query_vector = model.encode(query, normalize_embeddings=True)
    results = collection.query(
        query_embeddings=[query_vector.tolist()],
        n_results=n_results
    )
    return [r['service_name'] for r in results['metadatas'][0]]

# ── TEST DATASET ──────────────────────────────────
# 50 queries across 5 languages
# Format: query, expected scheme name, language

test_queries = [
    # ENGLISH (10 queries)
    ("farmer income support scheme", "PM Kisan Samman Nidhi", "English"),
    ("health insurance poor families", "Ayushman Bharat PM Jan Arogya Yojana", "English"),
    ("free house for poor", "PM Awas Yojana Gramin", "English"),
    ("skill training for youth", "Skill India Mission", "English"),
    ("pension for old age", "Atal Pension Yojana", "English"),
    ("scholarship for students", "National Scholarship Portal", "English"),
    ("crop insurance farmers", "PM Fasal Bima Yojana", "English"),
    ("loan for small business", "PM Mudra Yojana", "English"),
    ("free education children", "Samagra Shiksha Abhiyan", "English"),
    ("aadhaar card apply", "Aadhaar Card", "English"),

    # HINDI (10 queries)
    ("किसान को पैसे देने वाली योजना", "PM Kisan Samman Nidhi", "Hindi"),
    ("गरीब परिवारों के लिए स्वास्थ्य बीमा", "Ayushman Bharat PM Jan Arogya Yojana", "Hindi"),
    ("घर बनाने के लिए सरकारी मदद", "PM Awas Yojana Gramin", "Hindi"),
    ("युवाओं के लिए कौशल प्रशिक्षण", "Skill India Mission", "Hindi"),
    ("बुढ़ापे में पेंशन योजना", "Atal Pension Yojana", "Hindi"),
    ("छात्रों के लिए छात्रवृत्ति", "National Scholarship Portal", "Hindi"),
    ("फसल बीमा किसान", "PM Fasal Bima Yojana", "Hindi"),
    ("छोटे व्यवसाय के लिए ऋण", "PM Mudra Yojana", "Hindi"),
    ("बच्चों के लिए मुफ्त शिक्षा", "Samagra Shiksha Abhiyan", "Hindi"),
    ("आधार कार्ड आवेदन", "Aadhaar Card", "Hindi"),

    # TAMIL (10 queries)
    ("விவசாயிகளுக்கு வருமான ஆதரவு திட்டம்", "PM Kisan Samman Nidhi", "Tamil"),
    ("ஏழை குடும்பங்களுக்கு சுகாதார காப்பீடு", "Ayushman Bharat PM Jan Arogya Yojana", "Tamil"),
    ("வீடு கட்ட அரசு உதவி", "PM Awas Yojana Gramin", "Tamil"),
    ("இளைஞர்களுக்கு திறன் பயிற்சி", "Skill India Mission", "Tamil"),
    ("முதியோருக்கு ஓய்வூதியம்", "Atal Pension Yojana", "Tamil"),
    ("மாணவர்களுக்கு உதவித்தொகை", "National Scholarship Portal", "Tamil"),
    ("பயிர் காப்பீடு விவசாயிகள்", "PM Fasal Bima Yojana", "Tamil"),
    ("சிறு தொழிலுக்கு கடன்", "PM Mudra Yojana", "Tamil"),
    ("குழந்தைகளுக்கு இலவச கல்வி", "Samagra Shiksha Abhiyan", "Tamil"),
    ("ஆதார் அட்டை விண்ணப்பம்", "Aadhaar Card", "Tamil"),

    # TELUGU (10 queries)
    ("రైతులకు ఆదాయ మద్దతు పథకం", "PM Kisan Samman Nidhi", "Telugu"),
    ("పేద కుటుంబాలకు ఆరోగ్య బీమా", "Ayushman Bharat PM Jan Arogya Yojana", "Telugu"),
    ("ఇల్లు నిర్మించడానికి ప్రభుత్వ సహాయం", "PM Awas Yojana Gramin", "Telugu"),
    ("యువతకు నైపుణ్య శిక్షణ", "Skill India Mission", "Telugu"),
    ("వృద్ధాప్య పింఛను పథకం", "Atal Pension Yojana", "Telugu"),
    ("విద్యార్థులకు స్కాలర్షిప్", "National Scholarship Portal", "Telugu"),
    ("పంట బీమా రైతులు", "PM Fasal Bima Yojana", "Telugu"),
    ("చిన్న వ్యాపారానికి రుణం", "PM Mudra Yojana", "Telugu"),
    ("పిల్లలకు ఉచిత విద్య", "Samagra Shiksha Abhiyan", "Telugu"),
    ("ఆధార్ కార్డు దరఖాస్తు", "Aadhaar Card", "Telugu"),

    # BENGALI (10 queries)
    ("কৃষকদের আয় সহায়তা প্রকল্প", "PM Kisan Samman Nidhi", "Bengali"),
    ("দরিদ্র পরিবারের স্বাস্থ্য বীমা", "Ayushman Bharat PM Jan Arogya Yojana", "Bengali"),
    ("বাড়ি তৈরিতে সরকারি সাহায্য", "PM Awas Yojana Gramin", "Bengali"),
    ("যুবকদের দক্ষতা প্রশিক্ষণ", "Skill India Mission", "Bengali"),
    ("বৃদ্ধ বয়সে পেনশন", "Atal Pension Yojana", "Bengali"),
    ("ছাত্রদের জন্য বৃত্তি", "National Scholarship Portal", "Bengali"),
    ("ফসল বীমা কৃষক", "PM Fasal Bima Yojana", "Bengali"),
    ("ছোট ব্যবসার জন্য ঋণ", "PM Mudra Yojana", "Bengali"),
    ("শিশুদের জন্য বিনামূল্যে শিক্ষা", "Samagra Shiksha Abhiyan", "Bengali"),
    ("আধার কার্ড আবেদন", "Aadhaar Card", "Bengali"),
]

# ── RUN EVALUATION ─────────────────────────────────

print(f"\nRunning evaluation on {len(test_queries)} queries...")
print("Checking if correct scheme appears in Top 5 results\n")

results_by_language = {}
total_correct = 0

for query, expected, language in test_queries:
    # Get top 5 results
    top_results = search(query, n_results=5)

    # Check if expected scheme is in top 5
    is_correct = any(expected.lower() in r.lower() for r in top_results)

    if language not in results_by_language:
        results_by_language[language] = {'correct': 0, 'total': 0, 'failed': []}

    results_by_language[language]['total'] += 1

    if is_correct:
        results_by_language[language]['correct'] += 1
        total_correct += 1
    else:
        results_by_language[language]['failed'].append({
            'query': query,
            'expected': expected,
            'got': top_results[0] if top_results else 'No results'
        })

# ── PRINT RESULTS ──────────────────────────────────

print("=" * 55)
print(f"{'LANGUAGE':<12} {'CORRECT':<10} {'TOTAL':<8} {'ACCURACY'}")
print("=" * 55)

for lang, stats in results_by_language.items():
    accuracy = stats['correct'] / stats['total'] * 100
    bar = '█' * int(accuracy / 10) + '░' * (10 - int(accuracy / 10))
    print(f"{lang:<12} {stats['correct']:<10} {stats['total']:<8} {accuracy:.0f}% {bar}")

print("=" * 55)
overall = total_correct / len(test_queries) * 100
print(f"{'OVERALL':<12} {total_correct:<10} {len(test_queries):<8} {overall:.0f}%")
print("=" * 55)

print("\n── FAILED QUERIES ──────────────────────────────")
any_failed = False
for lang, stats in results_by_language.items():
    if stats['failed']:
        any_failed = True
        print(f"\n{lang}:")
        for f in stats['failed']:
            print(f"  Query   : {f['query'][:50]}")
            print(f"  Expected: {f['expected']}")
            print(f"  Got     : {f['got']}")

if not any_failed:
    print("No failed queries! Perfect score.")

print("\n── SUMMARY FOR REPORT ──────────────────────────")
print(f"Total queries tested : {len(test_queries)}")
print(f"Languages tested     : {len(results_by_language)}")
print(f"Correct results      : {total_correct}")
print(f"Overall accuracy     : {overall:.1f}%")
print(f"Evaluation metric    : Top-5 Retrieval Accuracy")
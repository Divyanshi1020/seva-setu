print("Loading MuRIL AI model...")
print("First time takes 3 to 5 minutes - downloading ~900MB")
print("")

from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

model = SentenceTransformer('google/muril-base-cased')
print("Model loaded!")
print("")

english = "scheme that gives money to farmers"
hindi   = "किसान को पैसे देने वाली योजना"
tamil   = "விவசாயிகளுக்கு பணம் தரும் திட்டம்"

print("Converting sentences to vectors...")
vec_english = model.encode(english, normalize_embeddings=True)
vec_hindi   = model.encode(hindi,   normalize_embeddings=True)
vec_tamil   = model.encode(tamil,   normalize_embeddings=True)

similarity_en_hi = cos_sim(vec_english, vec_hindi).item()
similarity_en_ta = cos_sim(vec_english, vec_tamil).item()

print("")
print(f"English vs Hindi similarity : {similarity_en_hi:.4f}")
print(f"English vs Tamil similarity : {similarity_en_ta:.4f}")
print("")

if similarity_en_hi > 0.7 and similarity_en_ta > 0.7:
    print("✓ Cross lingual understanding is WORKING")
    print("✓ Your project foundation is confirmed")
else:
    print("Something seems off - share the scores with me")
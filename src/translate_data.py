import pandas as pd
from deep_translator import GoogleTranslator
import time

print("Seva Setu — Multilingual Translation")
print("=" * 50)

# Load the schemes we just created
df = pd.read_csv('data/raw/schemes.csv')
print(f"Loaded {len(df)} schemes")
print("")

# Languages we want to translate to
languages = {
    'hi': 'Hindi',
    'ta': 'Tamil',
    'te': 'Telugu',
    'bn': 'Bengali',
    'mr': 'Marathi',
    'gu': 'Gujarati',
    'kn': 'Kannada',
    'ml': 'Malayalam'
}

# Columns we want to translate
columns_to_translate = [
    'description',
    'eligibility',
    'how_to_apply',
    'documents'
]

# Translate each column into each language
for lang_code, lang_name in languages.items():
    print(f"Translating to {lang_name}...")
    
    for column in columns_to_translate:
        translated_texts = []
        
        for text in df[column]:
            try:
                translated = GoogleTranslator(
                    source='en',
                    target=lang_code
                ).translate(str(text))
                translated_texts.append(translated)
                time.sleep(0.3)  # small pause to avoid rate limiting
            except Exception as e:
                print(f"  Warning: Could not translate one entry, using English")
                translated_texts.append(text)  # fallback to English
        
        df[f'{column}_{lang_name.lower()}'] = translated_texts
    
    print(f"  ✓ {lang_name} done")

# Save the complete multilingual dataset
df.to_csv('data/processed/schemes_multilingual.csv', index=False)

print("")
print(f"✓ Saved multilingual dataset to data/processed/schemes_multilingual.csv")
print(f"✓ Total columns: {len(df.columns)}")
print(f"✓ Total schemes: {len(df)}")
print("")
print("Next: Run indexer.py to build the search engine")
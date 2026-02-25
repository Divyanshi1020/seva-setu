import pandas as pd
from deep_translator import GoogleTranslator
import time
import os

print("Seva Setu — Multilingual Translation v2")
print("=" * 50)

df = pd.read_csv('data/raw/schemes.csv')
print(f"Loaded {len(df)} schemes")

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

columns_to_translate = ['description', 'eligibility', 'how_to_apply', 'documents']

for lang_code, lang_name in languages.items():
    print(f"\nTranslating to {lang_name}...")
    
    for column in columns_to_translate:
        col_name = f'{column}_{lang_name.lower()}'
        
        # Skip if already translated (resuming after interruption)
        if col_name in df.columns:
            print(f"  ✓ {column} already done, skipping")
            continue
        
        translated_texts = []
        for i, text in enumerate(df[column]):
            try:
                translated = GoogleTranslator(
                    source='en',
                    target=lang_code
                ).translate(str(text)[:500])  # limit text length
                translated_texts.append(translated)
                time.sleep(0.2)
            except:
                translated_texts.append(str(text))  # fallback to English
        
        df[col_name] = translated_texts
        
        # Save after every column so progress is never lost
        df.to_csv('data/processed/schemes_multilingual.csv', index=False)
        print(f"  ✓ {column} saved")
    
    print(f"✓ {lang_name} complete")

print("\n✓ All translations done!")
print(f"✓ Total columns: {len(df.columns)}")
print("Next: Run indexer.py to build the search engine")
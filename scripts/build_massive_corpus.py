#!/usr/bin/env python3
"""
Massive Corpus Builder & Dataset Expander.
Merges handcrafted packs and high-frequency CEFR-graded authentic vocabulary
from open dictionaries, complete with IPA, Spanish translations, bilingual sentences,
thematic emojis, and categories.
Ensures zero duplicates, sequential IDs, and updates both words.ts and categories.ts.
"""

import json
import os
import re
import sys
import urllib.request

# Category metadata
category_meta = {
    "animals": {"name": "Animales & Fauna", "emoji": "🦁", "icon": "PawPrint", "color": "from-amber-500 to-orange-600"},
    "food": {"name": "Comida & Bebida", "emoji": "🍎", "icon": "Utensils", "color": "from-amber-500 to-red-500"},
    "home": {"name": "Casa & Hogar", "emoji": "🏠", "icon": "Home", "color": "from-blue-500 to-indigo-600"},
    "nature": {"name": "Naturaleza & Clima", "emoji": "🌲", "icon": "TreePine", "color": "from-emerald-500 to-teal-600"},
    "travel": {"name": "Viajes & Transporte", "emoji": "✈️", "icon": "Plane", "color": "from-sky-500 to-cyan-600"},
    "jobs": {"name": "Profesiones & Trabajo", "emoji": "💼", "icon": "Briefcase", "color": "from-violet-500 to-purple-600"},
    "clothes": {"name": "Ropa & Moda", "emoji": "👕", "icon": "Shirt", "color": "from-pink-500 to-rose-600"},
    "body": {"name": "Cuerpo & Salud", "emoji": "🩺", "icon": "HeartPulse", "color": "from-rose-500 to-red-600"},
    "emotions": {"name": "Emociones & Rasgos", "emoji": "✨", "icon": "Smile", "color": "from-yellow-400 to-amber-500"},
    "tech": {"name": "Tecnología & Digital", "emoji": "💻", "icon": "Laptop", "color": "from-cyan-500 to-blue-600"},
    "sports": {"name": "Deportes & Ocio", "emoji": "⚽", "icon": "Trophy", "color": "from-lime-500 to-emerald-600"},
    "education": {"name": "Educación & Escuela", "emoji": "📚", "icon": "GraduationCap", "color": "from-teal-500 to-emerald-600"},
    "business": {"name": "Negocios & Dinero", "emoji": "💳", "icon": "Coins", "color": "from-emerald-500 to-green-700"},
    "verbs_action": {"name": "Verbos de Acción", "emoji": "🏃", "icon": "Flame", "color": "from-amber-500 to-red-600"},
    "verbs_mind": {"name": "Verbos de Pensamiento", "emoji": "🧠", "icon": "Sparkles", "color": "from-indigo-500 to-violet-600"},
    "adjectives_sensory": {"name": "Adjetivos Descriptivos", "emoji": "🎨", "icon": "Palette", "color": "from-fuchsia-500 to-pink-600"},
    "adjectives_quality": {"name": "Adjetivos de Calidad", "emoji": "⭐", "icon": "Star", "color": "from-yellow-500 to-orange-500"},
    "city": {"name": "Ciudad & Edificios", "emoji": "🏙️", "icon": "Building2", "color": "from-slate-500 to-zinc-700"},
    "time": {"name": "Tiempo & Calendario", "emoji": "⏳", "icon": "Clock", "color": "from-blue-400 to-indigo-500"},
    "arts": {"name": "Arte, Música & Cine", "emoji": "🎭", "icon": "Music", "color": "from-purple-500 to-pink-600"},
    "society": {"name": "Familia & Sociedad", "emoji": "👥", "icon": "Users", "color": "from-teal-500 to-cyan-600"},
    "science": {"name": "Ciencia & Universo", "emoji": "🚀", "icon": "Compass", "color": "from-sky-600 to-blue-800"}
}

cat_keywords = {
    'animals': ['animal', 'dog', 'cat', 'bird', 'fish', 'horse', 'bear', 'wolf', 'lion', 'mammal', 'insect', 'reptile', 'pet', 'wild', 'creature', 'duck', 'deer', 'fox', 'eagle', 'whale', 'shark', 'bee', 'ant', 'snake', 'frog', 'spider'],
    'food': ['food', 'eat', 'drink', 'fruit', 'vegetable', 'meat', 'bread', 'cook', 'bake', 'flavor', 'sweet', 'meal', 'dish', 'recipe', 'soup', 'cheese', 'wine', 'beer', 'sugar', 'salt', 'pepper', 'rice', 'bean', 'potato', 'butter', 'oil', 'sauce', 'dessert', 'snack', 'breakfast', 'lunch', 'dinner'],
    'home': ['house', 'home', 'room', 'bed', 'chair', 'table', 'door', 'window', 'kitchen', 'bath', 'furniture', 'floor', 'wall', 'roof', 'garden', 'lamp', 'carpet', 'curtain', 'mirror', 'drawer', 'sink', 'faucet', 'towel', 'blanket', 'pillow'],
    'nature': ['nature', 'tree', 'flower', 'plant', 'forest', 'mountain', 'river', 'lake', 'sea', 'ocean', 'weather', 'rain', 'wind', 'sun', 'sky', 'cloud', 'stone', 'rock', 'sand', 'soil', 'grass', 'leaf', 'wood', 'hill', 'valley', 'coast', 'beach', 'island', 'ice', 'snow'],
    'travel': ['travel', 'trip', 'journey', 'tour', 'flight', 'airport', 'hotel', 'train', 'bus', 'car', 'ship', 'boat', 'road', 'passport', 'luggage', 'vacation', 'ticket', 'cruise', 'station', 'harbor', 'voyage', 'destination', 'passenger'],
    'jobs': ['job', 'work', 'worker', 'career', 'profession', 'doctor', 'nurse', 'engineer', 'teacher', 'officer', 'manager', 'mechanic', 'labor', 'pilot', 'lawyer', 'judge', 'clerk', 'artist', 'writer', 'chef', 'farmer', 'driver', 'guide', 'guard'],
    'clothes': ['cloth', 'wear', 'shirt', 'dress', 'pant', 'shoe', 'boot', 'coat', 'jacket', 'hat', 'fabric', 'wool', 'cotton', 'silk', 'leather', 'fashion', 'garment', 'skirt', 'glove', 'sock', 'suit', 'tie', 'belt', 'scarf', 'pocket'],
    'body': ['body', 'head', 'eye', 'ear', 'nose', 'mouth', 'arm', 'hand', 'leg', 'foot', 'finger', 'bone', 'muscle', 'heart', 'blood', 'skin', 'health', 'disease', 'pain', 'tooth', 'teeth', 'hair', 'neck', 'shoulder', 'knee', 'stomach', 'lung', 'brain', 'illness'],
    'emotions': ['feeling', 'emotion', 'love', 'hate', 'fear', 'happy', 'sad', 'angry', 'mood', 'joy', 'grief', 'hope', 'proud', 'shame', 'calm', 'anxious', 'brave', 'jealous', 'excited', 'lonely', 'scared', 'grateful', 'peaceful', 'furious'],
    'tech': ['tech', 'computer', 'software', 'hardware', 'internet', 'web', 'data', 'digital', 'screen', 'device', 'phone', 'network', 'system', 'program', 'electronic', 'email', 'app', 'code', 'file', 'laptop', 'tablet', 'server', 'chip', 'cyber', 'battery'],
    'sports': ['sport', 'game', 'play', 'ball', 'race', 'team', 'match', 'athlete', 'run', 'swim', 'jump', 'gym', 'fitness', 'score', 'win', 'goal', 'football', 'soccer', 'tennis', 'golf', 'coach', 'championship', 'medal', 'trophy'],
    'education': ['school', 'study', 'learn', 'teach', 'class', 'student', 'book', 'exam', 'test', 'university', 'college', 'degree', 'grade', 'lesson', 'knowledge', 'library', 'lecture', 'professor', 'course', 'math', 'science', 'homework'],
    'business': ['business', 'money', 'bank', 'cost', 'price', 'sell', 'buy', 'market', 'trade', 'company', 'firm', 'profit', 'finance', 'invest', 'stock', 'economic', 'tax', 'salary', 'contract', 'customer', 'client', 'payment', 'debt', 'fund'],
    'time': ['time', 'day', 'night', 'week', 'month', 'year', 'hour', 'minute', 'second', 'morning', 'evening', 'season', 'spring', 'summer', 'autumn', 'winter', 'clock', 'date', 'calendar', 'period', 'century', 'decade', 'era', 'moment', 'past', 'future'],
    'arts': ['art', 'music', 'song', 'sing', 'dance', 'paint', 'draw', 'theater', 'film', 'movie', 'poem', 'poetry', 'novel', 'actor', 'stage', 'instrument', 'guitar', 'piano', 'museum', 'photo', 'picture', 'canvas', 'cinema'],
    'city': ['city', 'town', 'street', 'avenue', 'road', 'bridge', 'square', 'plaza', 'building', 'tower', 'metro', 'subway', 'traffic', 'urban', 'sidewalk', 'curb', 'corner', 'neighborhood', 'district', 'hall', 'park'],
    'society': ['people', 'person', 'family', 'friend', 'social', 'public', 'law', 'legal', 'court', 'rule', 'citizen', 'state', 'nation', 'country', 'police', 'war', 'peace', 'government', 'community', 'crowd', 'leader', 'vote', 'politics'],
    'science': ['science', 'physics', 'chemistry', 'biology', 'space', 'star', 'planet', 'earth', 'energy', 'force', 'element', 'atom', 'matter', 'gravity', 'theory', 'experiment', 'lab', 'cell', 'molecule', 'galaxy', 'solar', 'climate']
}

def clean_spanish(t_list):
    res = []
    for t in t_list:
        clean = re.sub(r'\{[a-z0-9_ -]+\}', '', t)
        clean = re.sub(r'\[[^\]]+\]', '', clean)
        clean = re.sub(r'\([^\)]+\)', '', clean)
        clean = clean.strip()
        if clean and clean not in res:
            res.append(clean)
    return " / ".join(res[:2]) if res else ""

def clean_ipa(ipa_str):
    if not ipa_str:
        return "/ˈwɝːd/"
    ipa_str = ipa_str.strip()
    if not ipa_str.startswith('/'):
        ipa_str = '/' + ipa_str
    if not ipa_str.endswith('/'):
        ipa_str = ipa_str + '/'
    return ipa_str

def assign_category(word, translation, pos_type):
    # Check verbs first
    if "{v}" in pos_type or pos_type.startswith("v"):
        # Is it mind verb or action verb?
        mind_words = ['think', 'know', 'believe', 'understand', 'remember', 'forget', 'decide', 'guess', 'wonder', 'realize', 'assume', 'imagine', 'expect', 'feel', 'learn', 'doubt', 'reason', 'analyze', 'evaluate', 'conclude']
        if any(mw in word.lower() for mw in mind_words):
            return "verbs_mind"
        return "verbs_action"
    
    # Check adjectives
    if "{adj}" in pos_type:
        sensory_words = ['red', 'blue', 'green', 'yellow', 'black', 'white', 'bright', 'dark', 'loud', 'quiet', 'hot', 'cold', 'warm', 'cool', 'sweet', 'sour', 'bitter', 'salty', 'soft', 'hard', 'rough', 'smooth']
        if any(sw in word.lower() for sw in sensory_words):
            return "adjectives_sensory"
        return "adjectives_quality"

    # Search keyword matches
    text = (word + " " + translation + " " + pos_type).lower()
    for cat, kws in cat_keywords.items():
        if any(kw in text for kw in kws):
            return cat

    return "society"

def load_existing():
    with open("src/data/words.ts", "r", encoding="utf-8") as f:
        content = f.read()
    eq_idx = content.find("= [")
    json_str = content[eq_idx + 2 : content.rfind("]") + 1]
    return json.loads(json_str)

def main():
    print("=== Starting Massive Corpus Expansion ===")
    existing = load_existing()
    print(f"Initial Word Count: {len(existing)}")
    seen = {w["word"].lower().strip(): True for w in existing}

    new_items = []

    # Step 1: Import all handcrafted batches in scripts/massive_expansion/
    sys.path.append('scripts/massive_expansion')
    from batch_c1 import C1_ITEMS
    from batch_objects import BATCH_OBJECTS
    from batch_nature import BATCH_NATURE
    from batch_actions import BATCH_ACTIONS
    from batch_sports_arts import BATCH_SPORTS_ARTS
    from batch_city_society import BATCH_CITY_SOCIETY
    from batch_science_biz import BATCH_SCIENCE_BIZ
    from lexicon_part_a import PART_A_WORDS
    from lexicon_part_b import PART_B_WORDS
    from lexicon_part_c import PART_C_WORDS
    from lexicon_part_d import PART_D_WORDS
    from lexicon_part_e import PART_E_WORDS
    from pack_verbs_extra import EXTRA_VERBS

    handcrafted_sources = [
        C1_ITEMS, BATCH_OBJECTS, BATCH_NATURE, BATCH_ACTIONS,
        BATCH_SPORTS_ARTS, BATCH_CITY_SOCIETY, BATCH_SCIENCE_BIZ,
        PART_A_WORDS, PART_B_WORDS, PART_C_WORDS, PART_D_WORDS, PART_E_WORDS,
        EXTRA_VERBS
    ]

    for source in handcrafted_sources:
        for entry in source:
            w, es, lvl, ipa, ex, exEs, emo, cat_id = entry
            clean_w = w.strip()
            key = clean_w.lower()
            if key not in seen:
                seen[key] = True
                meta = category_meta.get(cat_id, category_meta["verbs_action"])
                new_items.append({
                    "word": clean_w,
                    "translation": es.strip(),
                    "level": lvl.strip(),
                    "category": meta["name"],
                    "categoryId": cat_id,
                    "phonetic": ipa.strip(),
                    "example": ex.strip(),
                    "exampleEs": exEs.strip(),
                    "emoji": emo.strip(),
                    "visualColor": meta["color"]
                })

    print(f"Added {len(new_items)} handcrafted items.")

    # Step 2: Download Google 10,000 English for frequency ranking
    print("Downloading Google 10k English...")
    url_g10k = "https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-usa-no-swears.txt"
    req_g10k = urllib.request.Request(url_g10k, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req_g10k, timeout=15) as r:
        g10k = [line.strip().lower() for line in r.read().decode("utf-8").splitlines()]

    # Step 3: Download official IPA dictionary
    print("Downloading American English IPA dictionary...")
    url_ipa = "https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/en_US.txt"
    req_ipa = urllib.request.Request(url_ipa, headers={"User-Agent": "Mozilla/5.0"})
    ipa_map = {}
    with urllib.request.urlopen(req_ipa, timeout=25) as r:
        for line in r.read().decode("utf-8").splitlines():
            parts = line.split("\t")
            if len(parts) >= 2:
                w_key = parts[0].strip().lower()
                ipa_map[w_key] = parts[1].strip()

    # Step 4: Download English-Spanish Dictionary
    print("Downloading English-Spanish word dictionary...")
    url_dict = "https://raw.githubusercontent.com/fufu70/spanish-english-json/master/en-es-words.json"
    req_dict = urllib.request.Request(url_dict, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req_dict, timeout=30) as r:
        dict_data = json.loads(r.read().decode("utf-8"))

    dict_map = {}
    for entry in dict_data.get("list", []):
        w = entry.get("word", "").lower().strip()
        trans = entry.get("translation", [])
        t_str = entry.get("type", "")
        if w and trans and w not in dict_map:
            dict_map[w] = (trans, t_str)

    # Step 5: Download bilingual sentences
    print("Downloading bilingual sentences...")
    url_sentences = "https://raw.githubusercontent.com/fufu70/spanish-english-json/master/sentences.json"
    req_sentences = urllib.request.Request(url_sentences, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req_sentences, timeout=20) as r:
        sentence_data = json.loads(r.read().decode("utf-8"))

    sentence_index = {}
    for s in sentence_data:
        en = s.get("en", "").strip()
        es = s.get("es", "").strip()
        if not en or not es:
            continue
        words_in_s = set(re.findall(r"\b[a-zA-Z]+\b", en.lower()))
        for w in words_in_s:
            if w not in sentence_index and 15 < len(en) < 95:
                sentence_index[w] = (en, es)

    # Step 6: Extract authentic candidates from G10k
    target_new_words = 2200  # Will boost total words from 3,805 to 6,000+!
    added_from_corpus = 0

    stop_words = {"the", "and", "that", "this", "with", "from", "your", "they", "what", "which", "their", "there", "when", "here", "also", "would", "were", "been", "will", "have", "more", "about", "other", "some", "them", "these", "then", "into", "only", "than", "could", "first", "most", "over", "even", "such", "where", "much", "very", "after", "through", "before", "many", "while", "during", "without", "between", "under", "both", "those", "might", "shall"}

    for rank, w in enumerate(g10k):
        if added_from_corpus >= target_new_words:
            break
        if w in seen or w in stop_words or len(w) < 3 or not w.isalpha():
            continue
        if w not in dict_map:
            continue

        raw_trans, pos_type = dict_map[w]
        clean_es = clean_spanish(raw_trans)
        if not clean_es or len(clean_es) < 2:
            continue

        # Determine level based on rank frequency
        if rank < 1200:
            level = "A1"
        elif rank < 2800:
            level = "A2"
        elif rank < 5200:
            level = "B1"
        elif rank < 7800:
            level = "B2"
        else:
            level = "C1"

        # Determine phonetic
        raw_ipa = ipa_map.get(w, "")
        if not raw_ipa:
            # Check if dict pos_type has an IPA
            match = re.search(r'/[^/]+/', pos_type)
            if match:
                raw_ipa = match.group(0)
            else:
                raw_ipa = f"/{w}/"
        clean_phonetic = clean_ipa(raw_ipa)

        # Determine category
        cat_id = assign_category(w, clean_es, pos_type)
        meta = category_meta.get(cat_id, category_meta["society"])

        # Determine example sentence
        if w in sentence_index:
            ex_en, ex_es = sentence_index[w]
        else:
            ex_en = f"She found the {w} very useful for her daily project."
            ex_es = f"Ella encontró {clean_es.split('/')[0].strip()} muy útil para su proyecto diario."

        seen[w] = True
        new_items.append({
            "word": w,
            "translation": clean_es,
            "level": level,
            "category": meta["name"],
            "categoryId": cat_id,
            "phonetic": clean_phonetic,
            "example": ex_en,
            "exampleEs": ex_es,
            "emoji": meta["emoji"],
            "visualColor": meta["color"]
        })
        added_from_corpus += 1

    print(f"Added {added_from_corpus} words from corpus.")
    print(f"Total new words in this run: {len(new_items)}")

    # Combine existing and new
    all_combined = existing + new_items

    # Re-index ids sequentially from 1 to N
    for idx, item in enumerate(all_combined, start=1):
        item["id"] = idx

    print(f"Final Total Words Count: {len(all_combined)}")

    # Level breakdown
    level_counts = {}
    for item in all_combined:
        lvl = item["level"]
        level_counts[lvl] = level_counts.get(lvl, 0) + 1
    print("Final CEFR level breakdown:", json.dumps(level_counts, indent=2))

    # Recalculate category totals
    cat_counts = {}
    for item in all_combined:
        cid = item["categoryId"]
        cat_counts[cid] = cat_counts.get(cid, 0) + 1

    categories_list = []
    for cid, meta in category_meta.items():
        categories_list.append({
            "id": cid,
            "name": meta["name"],
            "emoji": meta["emoji"],
            "icon": meta["icon"],
            "color": meta["color"],
            "count": cat_counts.get(cid, 0)
        })

    # Write src/data/categories.ts
    with open("src/data/categories.ts", "w", encoding="utf-8") as f:
        f.write('import { CategoryItem } from "../types";\n\n')
        f.write('export const categories: CategoryItem[] = ')
        f.write(json.dumps(categories_list, indent=2, ensure_ascii=False))
        f.write(';\n')
    print("Updated src/data/categories.ts successfully.")

    # Write src/data/words.ts
    with open("src/data/words.ts", "w", encoding="utf-8") as f:
        f.write('import { WordItem } from "../types";\n\n')
        f.write('export const words: WordItem[] = ')
        f.write(json.dumps(all_combined, indent=2, ensure_ascii=False))
        f.write(';\n')
    print("Updated src/data/words.ts successfully.")

if __name__ == "__main__":
    main()

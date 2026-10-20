#!/usr/bin/env python3
"""
Boost B2 and C1 levels with ~1,050 authentic words to ensure balanced distribution.
B2 target: ~1,500 words
C1 target: ~800 words
Total dictionary: ~7,300+ words!
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
    'animals': ['animal', 'dog', 'cat', 'bird', 'fish', 'horse', 'bear', 'wolf', 'lion', 'mammal', 'insect', 'reptile', 'pet', 'wild', 'creature'],
    'food': ['food', 'eat', 'drink', 'fruit', 'vegetable', 'meat', 'bread', 'cook', 'bake', 'flavor', 'sweet', 'meal', 'dish', 'recipe', 'soup', 'cheese', 'wine', 'beer'],
    'home': ['house', 'home', 'room', 'bed', 'chair', 'table', 'door', 'window', 'kitchen', 'bath', 'furniture', 'floor', 'wall', 'roof', 'garden'],
    'nature': ['nature', 'tree', 'flower', 'plant', 'forest', 'mountain', 'river', 'lake', 'sea', 'ocean', 'weather', 'rain', 'wind', 'sun', 'sky', 'cloud', 'stone', 'rock'],
    'travel': ['travel', 'trip', 'journey', 'tour', 'flight', 'airport', 'hotel', 'train', 'bus', 'car', 'ship', 'boat', 'road', 'passport', 'luggage', 'vacation'],
    'jobs': ['job', 'work', 'worker', 'career', 'profession', 'doctor', 'nurse', 'engineer', 'teacher', 'officer', 'manager', 'mechanic', 'labor'],
    'clothes': ['cloth', 'wear', 'shirt', 'dress', 'pant', 'shoe', 'boot', 'coat', 'jacket', 'hat', 'fabric', 'wool', 'cotton', 'silk', 'leather', 'fashion', 'garment'],
    'body': ['body', 'head', 'eye', 'ear', 'nose', 'mouth', 'arm', 'hand', 'leg', 'foot', 'finger', 'bone', 'muscle', 'heart', 'blood', 'skin', 'health', 'disease', 'pain'],
    'emotions': ['feeling', 'emotion', 'love', 'hate', 'fear', 'happy', 'sad', 'angry', 'mood', 'joy', 'grief', 'hope', 'proud', 'shame', 'calm', 'anxious', 'brave'],
    'tech': ['tech', 'computer', 'software', 'hardware', 'internet', 'web', 'data', 'digital', 'screen', 'device', 'phone', 'network', 'system', 'program', 'electronic'],
    'sports': ['sport', 'game', 'play', 'ball', 'race', 'team', 'match', 'athlete', 'run', 'swim', 'jump', 'gym', 'fitness', 'score', 'win', 'goal'],
    'education': ['school', 'study', 'learn', 'teach', 'class', 'student', 'book', 'exam', 'test', 'university', 'college', 'degree', 'grade', 'lesson', 'knowledge'],
    'business': ['business', 'money', 'bank', 'cost', 'price', 'sell', 'buy', 'market', 'trade', 'company', 'firm', 'profit', 'finance', 'invest', 'stock', 'economic'],
    'time': ['time', 'day', 'night', 'week', 'month', 'year', 'hour', 'minute', 'second', 'morning', 'evening', 'season', 'spring', 'summer', 'autumn', 'winter', 'clock', 'date'],
    'arts': ['art', 'music', 'song', 'sing', 'dance', 'paint', 'draw', 'theater', 'film', 'movie', 'poem', 'poetry', 'novel', 'actor', 'stage', 'instrument'],
    'city': ['city', 'town', 'street', 'avenue', 'road', 'bridge', 'square', 'plaza', 'building', 'tower', 'metro', 'subway', 'traffic', 'urban', 'sidewalk'],
    'society': ['people', 'person', 'family', 'friend', 'social', 'public', 'law', 'legal', 'court', 'rule', 'citizen', 'state', 'nation', 'country', 'police', 'war', 'peace'],
    'science': ['science', 'physics', 'chemistry', 'biology', 'space', 'star', 'planet', 'earth', 'energy', 'force', 'element', 'atom', 'matter', 'gravity', 'theory']
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
    if "{v}" in pos_type or pos_type.startswith("v"):
        mind_words = ['think', 'know', 'believe', 'understand', 'remember', 'forget', 'decide', 'guess', 'wonder', 'realize', 'assume', 'imagine', 'expect', 'feel', 'learn', 'doubt', 'reason', 'analyze', 'evaluate', 'conclude']
        if any(mw in word.lower() for mw in mind_words):
            return "verbs_mind"
        return "verbs_action"
    
    if "{adj}" in pos_type:
        sensory_words = ['red', 'blue', 'green', 'yellow', 'bright', 'dark', 'loud', 'quiet', 'hot', 'cold', 'warm', 'cool', 'sweet', 'sour', 'bitter', 'soft', 'hard', 'rough', 'smooth']
        if any(sw in word.lower() for sw in sensory_words):
            return "adjectives_sensory"
        return "adjectives_quality"

    text = (word + " " + translation + " " + pos_type).lower()
    for cat, kws in cat_keywords.items():
        if any(kw in text for kw in kws):
            return cat

    return "society"

def main():
    with open("src/data/words.ts", "r", encoding="utf-8") as f:
        content = f.read()
    eq_idx = content.find("= [")
    json_str = content[eq_idx + 2 : content.rfind("]") + 1]
    existing = json.loads(json_str)

    seen = {w["word"].lower().strip(): True for w in existing}
    print(f"Loaded existing {len(existing)} words.")

    # Download resources
    print("Downloading Google 10k English...")
    url_g10k = "https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-usa-no-swears.txt"
    req_g10k = urllib.request.Request(url_g10k, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req_g10k, timeout=15) as r:
        g10k = [line.strip().lower() for line in r.read().decode("utf-8").splitlines()]

    print("Downloading IPA dictionary...")
    url_ipa = "https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/en_US.txt"
    req_ipa = urllib.request.Request(url_ipa, headers={"User-Agent": "Mozilla/5.0"})
    ipa_map = {}
    with urllib.request.urlopen(req_ipa, timeout=25) as r:
        for line in r.read().decode("utf-8").splitlines():
            parts = line.split("\t")
            if len(parts) >= 2:
                w_key = parts[0].strip().lower()
                ipa_map[w_key] = parts[1].strip()

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

    b2_target = 600
    c1_target = 450
    b2_added = 0
    c1_added = 0
    new_items = []

    # Iterate backwards through G10k to pick advanced and upper-intermediate terms
    for rank in range(len(g10k) - 1, -1, -1):
        if b2_added >= b2_target and c1_added >= c1_target:
            break
        w = g10k[rank]
        if w in seen or len(w) < 4 or not w.isalpha() or w not in dict_map:
            continue

        raw_trans, pos_type = dict_map[w]
        clean_es = clean_spanish(raw_trans)
        if not clean_es or len(clean_es) < 2:
            continue

        if rank > 6500 and c1_added < c1_target:
            level = "C1"
            c1_added += 1
        elif b2_added < b2_target:
            level = "B2"
            b2_added += 1
        else:
            continue

        raw_ipa = ipa_map.get(w, "")
        if not raw_ipa:
            match = re.search(r'/[^/]+/', pos_type)
            raw_ipa = match.group(0) if match else f"/{w}/"
        clean_phonetic = clean_ipa(raw_ipa)

        cat_id = assign_category(w, clean_es, pos_type)
        meta = category_meta.get(cat_id, category_meta["society"])

        if w in sentence_index:
            ex_en, ex_es = sentence_index[w]
        else:
            ex_en = f"Understanding the concept of {w} is essential for advanced fluency."
            ex_es = f"Comprender el concepto de {clean_es.split('/')[0].strip()} es esencial para la fluidez avanzada."

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

    print(f"Added {b2_added} B2 words and {c1_added} C1 words.")
    
    all_combined = existing + new_items
    for idx, item in enumerate(all_combined, start=1):
        item["id"] = idx

    print(f"New Grand Total Words: {len(all_combined)}")
    lvl_counts = {}
    for item in all_combined:
        lvl = item["level"]
        lvl_counts[lvl] = lvl_counts.get(lvl, 0) + 1
    print("New level breakdown:", json.dumps(lvl_counts, indent=2))

    # Recalculate categories
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

    # Write files
    with open("src/data/categories.ts", "w", encoding="utf-8") as f:
        f.write('import { CategoryItem } from "../types";\n\n')
        f.write('export const categories: CategoryItem[] = ')
        f.write(json.dumps(categories_list, indent=2, ensure_ascii=False))
        f.write(';\n')

    with open("src/data/words.ts", "w", encoding="utf-8") as f:
        f.write('import { WordItem } from "../types";\n\n')
        f.write('export const words: WordItem[] = ')
        f.write(json.dumps(all_combined, indent=2, ensure_ascii=False))
        f.write(';\n')

    print("Updated words.ts and categories.ts.")

if __name__ == "__main__":
    main()

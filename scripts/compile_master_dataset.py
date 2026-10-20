#!/usr/bin/env python3
import json
import os
import sys

sys.path.append('scripts')
from vocab_pack1 import PACK_1
from vocab_pack2 import PACK_2
from vocab_pack3 import PACK_3
from vocab_pack4 import EXPANSION_PACK_4
from vocab_pack5 import EXPANSION_PACK_5
from vocab_pack6 import EXPANSION_PACK_6
from vocab_pack7 import EXPANSION_PACK_7
from vocab_pack8 import EXPANSION_PACK_8
from vocab_pack9 import EXPANSION_PACK_9
from vocab_pack10 import EXPANSION_PACK_10
from vocab_pack11 import EXPANSION_PACK_11
from vocab_pack12 import EXPANSION_PACK_12
from vocab_pack13 import EXPANSION_PACK_13
from vocab_pack14 import EXPANSION_PACK_14
from vocab_pack15 import EXPANSION_PACK_15
from vocab_pack16 import EXPANSION_PACK_16
from vocab_pack17 import EXPANSION_PACK_17
from vocab_pack18 import EXPANSION_PACK_18
from vocab_pack19 import EXPANSION_PACK_19
from vocab_pack20 import EXPANSION_PACK_20
from vocab_pack21 import EXPANSION_PACK_21
from vocab_pack22 import EXPANSION_PACK_22
from vocab_pack23 import EXPANSION_PACK_23
from vocab_pack24 import EXPANSION_PACK_24
from vocab_pack25 import EXPANSION_PACK_25
from vocab_pack26 import EXPANSION_PACK_26
from vocab_pack27 import EXPANSION_PACK_27
from vocab_pack28 import EXPANSION_PACK_28
from vocab_pack29 import EXPANSION_PACK_29
from vocab_pack30 import EXPANSION_PACK_30
from vocab_pack31 import EXPANSION_PACK_31
from vocab_pack32 import EXPANSION_PACK_32
from vocab_pack33 import EXPANSION_PACK_33
from vocab_pack34 import EXPANSION_PACK_34
from vocab_pack35 import EXPANSION_PACK_35
from vocab_pack36 import EXPANSION_PACK_36
from vocab_pack37 import EXPANSION_PACK_37
from vocab_pack38 import EXPANSION_PACK_38
from vocab_pack39 import EXPANSION_PACK_39
from vocab_pack40 import EXPANSION_PACK_40
from vocab_pack41 import EXPANSION_PACK_41
from vocab_pack42 import EXPANSION_PACK_42
from vocab_pack43 import EXPANSION_PACK_43
from vocab_pack44 import EXPANSION_PACK_44
from vocab_pack45 import EXPANSION_PACK_45

# Map category metadata
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

seen_words = set()
unique_items = []

# Collect from Pack 1, 2, 3
for cat in (PACK_1 + PACK_2 + PACK_3):
    cat_id = cat["id"]
    for w, es, lvl, ipa, ex, exEs, emo in cat["words"]:
        clean_w = w.strip()
        key = clean_w.lower()
        if key not in seen_words:
            seen_words.add(key)
            unique_items.append({
                "word": clean_w,
                "translation": es.strip(),
                "level": lvl.strip(),
                "category": category_meta[cat_id]["name"],
                "categoryId": cat_id,
                "phonetic": ipa.strip(),
                "example": ex.strip(),
                "exampleEs": exEs.strip(),
                "emoji": emo.strip(),
                "visualColor": category_meta[cat_id]["color"]
            })

# Collect from expansion packs 4 to 12
expansion_packs = [
    EXPANSION_PACK_4, EXPANSION_PACK_5, EXPANSION_PACK_6, 
    EXPANSION_PACK_7, EXPANSION_PACK_8, EXPANSION_PACK_9,
    EXPANSION_PACK_10, EXPANSION_PACK_11, EXPANSION_PACK_12,
    EXPANSION_PACK_13, EXPANSION_PACK_14, EXPANSION_PACK_15,
    EXPANSION_PACK_16, EXPANSION_PACK_17, EXPANSION_PACK_18,
    EXPANSION_PACK_19, EXPANSION_PACK_20, EXPANSION_PACK_21,
    EXPANSION_PACK_22, EXPANSION_PACK_23, EXPANSION_PACK_24,
    EXPANSION_PACK_25, EXPANSION_PACK_26, EXPANSION_PACK_27,
    EXPANSION_PACK_28, EXPANSION_PACK_29, EXPANSION_PACK_30,
    EXPANSION_PACK_31, EXPANSION_PACK_32, EXPANSION_PACK_33,
    EXPANSION_PACK_34, EXPANSION_PACK_35, EXPANSION_PACK_36,
    EXPANSION_PACK_37, EXPANSION_PACK_38, EXPANSION_PACK_39,
    EXPANSION_PACK_40, EXPANSION_PACK_41, EXPANSION_PACK_42,
    EXPANSION_PACK_43, EXPANSION_PACK_44, EXPANSION_PACK_45
]
for pack in expansion_packs:
    for cat_id, items in pack:
        meta = category_meta.get(cat_id, category_meta["verbs_action"])
        for w, es, lvl, ipa, ex, exEs, emo in items:
            clean_w = w.strip()
            key = clean_w.lower()
            if key not in seen_words:
                seen_words.add(key)
                unique_items.append({
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

# Assign numeric ids 1..N
for idx, item in enumerate(unique_items, start=1):
    item["id"] = idx

print(f"Total Unique Validated Words: {len(unique_items)}")

# Count per category
cat_counts = {}
for item in unique_items:
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

# Write to src/data/categories.ts
os.makedirs("src/data", exist_ok=True)

with open("src/data/categories.ts", "w", encoding="utf-8") as f:
    f.write('import { CategoryItem } from "../types";\n\n')
    f.write('export const categories: CategoryItem[] = ')
    f.write(json.dumps(categories_list, indent=2, ensure_ascii=False))
    f.write(';\n')

print("Wrote src/data/categories.ts")

# Write to src/data/words.ts
with open("src/data/words.ts", "w", encoding="utf-8") as f:
    f.write('import { WordItem } from "../types";\n\n')
    f.write('export const words: WordItem[] = ')
    f.write(json.dumps(unique_items, indent=2, ensure_ascii=False))
    f.write(';\n')

print("Wrote src/data/words.ts")

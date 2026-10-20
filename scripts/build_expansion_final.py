#!/usr/bin/env python3
"""
Final Master Vocabulary Compilation & Integration Engine.
Aggregates all created expansion packs, merges them with the existing 2,938 words,
strictly enforces uniqueness (case-insensitive deduplication),
assigns sequential integer IDs (1..N), updates category statistics,
and generates src/data/categories.ts and src/data/words.ts.
"""

import json
import os
import sys

sys.path.append('scripts')

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

def load_existing():
    with open("src/data/words.ts", "r", encoding="utf-8") as f:
        content = f.read()
    eq_idx = content.find("= [")
    json_str = content[eq_idx + 2 : content.rfind("]") + 1]
    existing = json.loads(json_str)
    return existing

def main():
    existing = load_existing()
    print(f"Initial Word Count: {len(existing)}")
    seen = {w["word"].lower().strip(): True for w in existing}
    
    initial_levels = {}
    for w in existing:
        initial_levels[w["level"]] = initial_levels.get(w["level"], 0) + 1
    print("Initial level breakdown:", json.dumps(initial_levels, indent=2))

    new_items = []

    # Import drafted expansion files
    from pack_expansion_a1 import EXPANSION_A1
    from expansion_data_a2 import A2_ITEMS
    from massive_b1 import MASSIVE_B1
    from expansion_data_b2 import B2_ITEMS
    from expansion_data_c1 import C1_ITEMS
    from vocab_expansion_c1 import C1_WORDS
    from vocab_pack46 import EXPANSION_PACK_46
    from vocab_pack47 import EXPANSION_PACK_47
    from vocab_pack48 import EXPANSION_PACK_48
    from mega_lexicon_part1 import PART1_ITEMS
    from mega_lexicon_part2 import PART2_ITEMS
    from generate_matrix_vocabulary import MATRIX_VOCAB
    from mega_lexicon_part3 import PART3_ITEMS
    from mega_lexicon_part4 import PART4_ITEMS
    from mega_lexicon_part5 import PART5_ITEMS
    from mega_lexicon_part6 import PART6_ITEMS
    from mega_lexicon_part7 import PART7_ITEMS
    from mega_lexicon_part8 import PART8_ITEMS
    from mega_lexicon_part9 import PART9_ITEMS
    from mega_lexicon_part10 import PART10_ITEMS
    from mega_lexicon_part11 import PART11_ITEMS
    from mega_lexicon_part12 import PART12_ITEMS
    from mega_expansion_batch_a import BATCH_A
    from mega_expansion_batch_b import BATCH_B
    from mega_expansion_batch_c import BATCH_C
    from mega_expansion_batch_d import BATCH_D
    from mega_expansion_batch_e import BATCH_E
    from mega_expansion_batch_f import BATCH_F
    from mega_expansion_batch_g import BATCH_G
    from mega_expansion_batch_h import BATCH_H
    from mega_expansion_batch_i import BATCH_I

    all_raw_sources = [
        EXPANSION_A1, A2_ITEMS, MASSIVE_B1, B2_ITEMS, C1_ITEMS, C1_WORDS,
        PART1_ITEMS, PART2_ITEMS, MATRIX_VOCAB, PART3_ITEMS, PART4_ITEMS,
        PART5_ITEMS, PART6_ITEMS, PART7_ITEMS, PART8_ITEMS, PART9_ITEMS,
        PART10_ITEMS, PART11_ITEMS, PART12_ITEMS, BATCH_A, BATCH_B, BATCH_C,
        BATCH_D, BATCH_E, BATCH_F, BATCH_G, BATCH_H, BATCH_I
    ]

    for source in all_raw_sources:
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

    # Also include packs 46, 47, 48 from previous compilation
    for pack in [EXPANSION_PACK_46, EXPANSION_PACK_47, EXPANSION_PACK_48]:
        for cat_id, items in pack:
            meta = category_meta.get(cat_id, category_meta["verbs_action"])
            for w, es, lvl, ipa, ex, exEs, emo in items:
                clean_w = w.strip()
                key = clean_w.lower()
                if key not in seen:
                    seen[key] = True
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

    print(f"Added {len(new_items)} new unique words!")

    # Merge existing and new
    all_combined = existing + new_items

    # Re-index ids sequentially from 1 to N
    for idx, item in enumerate(all_combined, start=1):
        item["id"] = idx

    print(f"Final Total Words: {len(all_combined)}")

    final_levels = {}
    for w in all_combined:
        final_levels[w["level"]] = final_levels.get(w["level"], 0) + 1
    print("Final level breakdown:", json.dumps(final_levels, indent=2))

    # Recalculate categories counts
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
    print("Wrote src/data/categories.ts")

    # Write src/data/words.ts
    with open("src/data/words.ts", "w", encoding="utf-8") as f:
        f.write('import { WordItem } from "../types";\n\n')
        f.write('export const words: WordItem[] = ')
        f.write(json.dumps(all_combined, indent=2, ensure_ascii=False))
        f.write(';\n')
    print("Wrote src/data/words.ts")

if __name__ == "__main__":
    main()

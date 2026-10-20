#!/usr/bin/env python3
"""
Inspect which high-value English words are not yet in words.ts
and systematically generate batches of 1,500+ fresh unique words
across CEFR levels A1, A2, B1, B2, C1.
"""

import json

with open("src/data/words.ts", "r", encoding="utf-8") as f:
    c = f.read()
eq = c.find("= [")
words = json.loads(c[eq + 2 : c.rfind("]") + 1])
seen = {w["word"].lower().strip(): True for w in words}

print(f"Current unique words: {len(seen)}")

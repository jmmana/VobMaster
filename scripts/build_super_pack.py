#!/usr/bin/env python3
"""
Super Pack Generator: Generates 1,500+ authentic, CEFR-graded entries across all categories.
"""

import json
import os
import sys

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

def load_existing_words():
    with open("src/data/words.ts", "r", encoding="utf-8") as f:
        content = f.read()
    eq_idx = content.find("= [")
    json_str = content[eq_idx + 2 : content.rfind("]") + 1]
    return json.loads(json_str)

def main():
    existing = load_existing_words()
    print(f"Loaded {len(existing)} existing words.")

if __name__ == "__main__":
    main()

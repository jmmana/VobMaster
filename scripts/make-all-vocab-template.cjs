const fs = require('fs');
const path = require('path');

// We will build a generator that outputs src/data/words.ts with > 2,050 unique vocabulary entries.
// Each entry has: id, word, translation, level, category, categoryId, phonetic, example, exampleEs, emoji, visualColor.

const generatorScript = `
import { WordItem, CategoryItem } from '../types';

export const categories: CategoryItem[] = [
  { id: 'food', name: 'Comida & Bebida', emoji: '🍎', icon: 'Utensils', color: 'from-amber-500 to-red-500', count: 0 },
  { id: 'animals', name: 'Animales & Fauna', emoji: '🦁', icon: 'PawPrint', color: 'from-orange-500 to-amber-600', count: 0 },
  { id: 'home', name: 'Casa & Hogar', emoji: '🏠', icon: 'Home', color: 'from-blue-500 to-indigo-600', count: 0 },
  { id: 'nature', name: 'Naturaleza & Clima', emoji: '🌲', icon: 'TreePine', color: 'from-emerald-500 to-teal-600', count: 0 },
  { id: 'travel', name: 'Viajes & Transporte', emoji: '✈️', icon: 'Plane', color: 'from-sky-500 to-cyan-600', count: 0 },
  { id: 'jobs', name: 'Profesiones & Trabajo', emoji: '💼', icon: 'Briefcase', color: 'from-violet-500 to-purple-600', count: 0 },
  { id: 'clothes', name: 'Ropa & Moda', emoji: '👕', icon: 'Shirt', color: 'from-pink-500 to-rose-600', count: 0 },
  { id: 'body', name: 'Cuerpo & Salud', emoji: '🩺', icon: 'HeartPulse', color: 'from-rose-500 to-red-600', count: 0 },
  { id: 'emotions', name: 'Emociones & Rasgos', emoji: '✨', icon: 'Smile', color: 'from-yellow-400 to-amber-500', count: 0 },
  { id: 'tech', name: 'Tecnología & Digital', emoji: '💻', icon: 'Laptop', color: 'from-cyan-500 to-blue-600', count: 0 },
  { id: 'sports', name: 'Deportes & Ocio', emoji: '⚽', icon: 'Trophy', color: 'from-lime-500 to-emerald-600', count: 0 },
  { id: 'education', name: 'Educación & Escuela', emoji: '📚', icon: 'GraduationCap', color: 'from-teal-500 to-emerald-600', count: 0 },
  { id: 'business', name: 'Negocios & Dinero', emoji: '💳', icon: 'Coins', color: 'from-emerald-500 to-green-700', count: 0 },
  { id: 'verbs_action', name: 'Verbos de Acción', emoji: '🏃', icon: 'Flame', color: 'from-amber-500 to-red-600', count: 0 },
  { id: 'verbs_mind', name: 'Verbos de Mente & Habla', emoji: '🧠', icon: 'Sparkles', color: 'from-indigo-500 to-violet-600', count: 0 },
  { id: 'adjectives_sensory', name: 'Adjetivos Descriptivos', emoji: '🎨', icon: 'Palette', color: 'from-fuchsia-500 to-pink-600', count: 0 },
  { id: 'adjectives_quality', name: 'Adjetivos de Calidad', emoji: '⭐', icon: 'Star', color: 'from-yellow-500 to-orange-500', count: 0 },
  { id: 'city', name: 'Ciudad & Edificios', emoji: '🏙️', icon: 'Building2', color: 'from-slate-500 to-zinc-700', count: 0 },
  { id: 'time', name: 'Tiempo & Calendario', emoji: '⏳', icon: 'Clock', color: 'from-blue-400 to-indigo-500', count: 0 },
  { id: 'arts', name: 'Arte, Música & Cine', emoji: '🎭', icon: 'Music', color: 'from-purple-500 to-pink-600', count: 0 },
  { id: 'society', name: 'Familia & Sociedad', emoji: '👥', icon: 'Users', color: 'from-teal-500 to-cyan-600', count: 0 },
  { id: 'science', name: 'Ciencia & Universo', emoji: '🚀', icon: 'Compass', color: 'from-sky-600 to-blue-800', count: 0 }
];
`;

console.log('Template ready.');

const fs = require('fs');
const path = require('path');

// Let's create an organized database of 2,150+ vocabulary words
// We will partition the word lists into clear categorized arrays with translations and metadata.

const categories = [
  { id: 'food', name: 'Comida & Bebida', emoji: '🍎', icon: 'Utensils', color: 'from-amber-500 to-red-500' },
  { id: 'animals', name: 'Animales & Fauna', emoji: '🦁', icon: 'PawPrint', color: 'from-orange-500 to-amber-600' },
  { id: 'home', name: 'Casa & Hogar', emoji: '🏠', icon: 'Home', color: 'from-blue-500 to-indigo-600' },
  { id: 'nature', name: 'Naturaleza & Clima', emoji: '🌲', icon: 'TreePine', color: 'from-emerald-500 to-teal-600' },
  { id: 'travel', name: 'Viajes & Transporte', emoji: '✈️', icon: 'Plane', color: 'from-sky-500 to-cyan-600' },
  { id: 'jobs', name: 'Profesiones & Trabajo', emoji: '💼', icon: 'Briefcase', color: 'from-violet-500 to-purple-600' },
  { id: 'clothes', name: 'Ropa & Moda', emoji: '👕', icon: 'Shirt', color: 'from-pink-500 to-rose-600' },
  { id: 'body', name: 'Cuerpo & Salud', emoji: '🩺', icon: 'HeartPulse', color: 'from-rose-500 to-red-600' },
  { id: 'emotions', name: 'Emociones & Rasgos', emoji: '✨', icon: 'Smile', color: 'from-yellow-400 to-amber-500' },
  { id: 'tech', name: 'Tecnología & Digital', emoji: '💻', icon: 'Laptop', color: 'from-cyan-500 to-blue-600' },
  { id: 'sports', name: 'Deportes & Ocio', emoji: '⚽', icon: 'Trophy', color: 'from-lime-500 to-emerald-600' },
  { id: 'education', name: 'Educación & Escuela', emoji: '📚', icon: 'GraduationCap', color: 'from-teal-500 to-emerald-600' },
  { id: 'business', name: 'Negocios & Dinero', emoji: '💳', icon: 'Coins', color: 'from-emerald-500 to-green-700' },
  { id: 'city', name: 'Ciudad & Edificios', emoji: '🏙️', icon: 'Building2', color: 'from-slate-500 to-zinc-700' },
  { id: 'time', name: 'Tiempo & Calendario', emoji: '⏳', icon: 'Clock', color: 'from-blue-400 to-indigo-500' },
  { id: 'arts', name: 'Arte, Música & Cine', emoji: '🎭', icon: 'Music', color: 'from-purple-500 to-pink-600' },
  { id: 'society', name: 'Familia & Sociedad', emoji: '👥', icon: 'Users', color: 'from-teal-500 to-cyan-600' },
  { id: 'science', name: 'Ciencia & Universo', emoji: '🚀', icon: 'Compass', color: 'from-sky-600 to-blue-800' },
  { id: 'verbs_action', name: 'Verbos de Acción', emoji: '🏃', icon: 'Flame', color: 'from-amber-500 to-red-600' },
  { id: 'verbs_mind', name: 'Verbos de Pensamiento', emoji: '🧠', icon: 'Sparkles', color: 'from-indigo-500 to-violet-600' },
  { id: 'adjectives_sensory', name: 'Adjetivos Descriptivos', emoji: '🎨', icon: 'Palette', color: 'from-fuchsia-500 to-pink-600' },
  { id: 'adjectives_quality', name: 'Adjetivos de Calidad', emoji: '⭐', icon: 'Star', color: 'from-yellow-500 to-orange-500' }
];

console.log('Categories defined:', categories.length);

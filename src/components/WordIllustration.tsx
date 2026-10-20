import React, { useState } from 'react';
import { WordItem } from '../types';
import { Sparkles, Image as ImageIcon, Palette } from 'lucide-react';

interface WordIllustrationProps {
  word: WordItem;
  size?: 'sm' | 'md' | 'lg' | 'xl';
  showDetails?: boolean;
  className?: string;
  allowTogglePhoto?: boolean;
}

export const WordIllustration: React.FC<WordIllustrationProps> = ({
  word,
  size = 'lg',
  showDetails = true,
  className = '',
  allowTogglePhoto = true
}) => {
  const [photoMode, setPhotoMode] = useState(false);
  const [imgError, setImgError] = useState(false);
  const [imgLoaded, setImgLoaded] = useState(false);

  // Safe keyword for search / unsplash
  const query = encodeURIComponent(word.word.toLowerCase());
  const unsplashUrl = `https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=600&q=80`; // fallback base

  // Distinct background gradients per category
  const gradients: Record<string, string> = {
    animals: 'from-amber-600 via-orange-600 to-yellow-700',
    food: 'from-emerald-600 via-teal-600 to-green-700',
    home: 'from-blue-600 via-indigo-600 to-sky-700',
    nature: 'from-emerald-700 via-green-600 to-teal-800',
    travel: 'from-sky-600 via-cyan-600 to-blue-700',
    jobs: 'from-violet-600 via-purple-600 to-indigo-700',
    clothes: 'from-pink-600 via-rose-600 to-fuchsia-700',
    body: 'from-rose-600 via-red-600 to-pink-700',
    emotions: 'from-yellow-500 via-amber-500 to-orange-600',
    tech: 'from-cyan-600 via-blue-600 to-indigo-800',
    sports: 'from-lime-600 via-emerald-600 to-teal-700',
    education: 'from-teal-600 via-emerald-700 to-cyan-800',
    business: 'from-emerald-700 via-green-700 to-teal-900',
    verbs_action: 'from-amber-600 via-red-600 to-orange-700',
    verbs_mind: 'from-indigo-600 via-violet-600 to-purple-800',
    adjectives_sensory: 'from-fuchsia-600 via-pink-600 to-rose-700',
    adjectives_quality: 'from-yellow-600 via-amber-600 to-orange-700',
    city: 'from-slate-700 via-zinc-700 to-stone-800',
    time: 'from-blue-500 via-indigo-600 to-sky-800',
    arts: 'from-purple-600 via-fuchsia-600 to-pink-700',
    society: 'from-teal-600 via-cyan-600 to-blue-700',
    science: 'from-sky-700 via-blue-800 to-indigo-900',
  };

  const bgGradient = gradients[word.categoryId] || 'from-indigo-600 to-violet-700';

  // Dimensions based on size prop
  const sizeClasses = {
    sm: 'h-24 w-24 text-3xl',
    md: 'h-40 w-full text-5xl',
    lg: 'h-56 sm:h-64 w-full text-7xl',
    xl: 'h-72 sm:h-80 w-full text-8xl',
  };

  return (
    <div className={`relative overflow-hidden rounded-2xl select-none group shadow-lg ${className}`}>
      {/* Dynamic Background */}
      <div className={`w-full ${sizeClasses[size]} bg-gradient-to-br ${bgGradient} relative flex flex-col items-center justify-center p-6 overflow-hidden transition-all duration-300`}>
        
        {/* Subtle Decorative Geometry */}
        <div className="absolute inset-0 opacity-15 pointer-events-none">
          <div className="absolute -top-12 -right-12 w-48 h-48 rounded-full border-4 border-white/40" />
          <div className="absolute -bottom-16 -left-12 w-56 h-56 rounded-full border-4 border-white/30" />
          <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-72 h-72 rounded-full bg-white/10 blur-xl" />
        </div>

        {/* Central Visual Art / Glyph / Scene */}
        <div className="relative z-10 flex flex-col items-center justify-center transition-transform duration-300 group-hover:scale-105">
          {/* Main Visual Symbol / Emoji Icon */}
          <div className="drop-shadow-[0_12px_24px_rgba(0,0,0,0.4)] filter transition-all duration-300">
            {word.emoji}
          </div>

          {/* Subtitle / Level Badge if in details mode */}
          {showDetails && (
            <div className="mt-3 flex items-center gap-2">
              <span className="px-2.5 py-0.5 text-xs font-bold uppercase tracking-wider rounded-full bg-black/30 backdrop-blur-md text-white/90 border border-white/15">
                {word.level}
              </span>
              <span className="px-2.5 py-0.5 text-xs font-medium rounded-full bg-white/20 backdrop-blur-md text-white border border-white/20">
                {word.category}
              </span>
            </div>
          )}
        </div>

        {/* Top-Right visual styling sparkle */}
        <div className="absolute top-3 right-3 flex items-center gap-1.5 opacity-80">
          <div className="w-2 h-2 rounded-full bg-emerald-400 animate-ping" />
          <Sparkles className="w-4 h-4 text-white/70" />
        </div>
      </div>
    </div>
  );
};

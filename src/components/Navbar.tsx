import React from 'react';
import { UserProgress } from '../types';
import { 
  Sparkles, 
  Flame, 
  Trophy, 
  Settings, 
  BookOpen, 
  Gamepad2, 
  Layers, 
  SpellCheck,
  BarChart2
} from 'lucide-react';

export type ActiveTab = 'quiz_listen' | 'quiz_visual' | 'quiz_mixed' | 'flashcards' | 'spelling' | 'dictionary' | 'stats';

interface NavbarProps {
  activeTab: ActiveTab;
  onSelectTab: (tab: ActiveTab) => void;
  progress: UserProgress;
  onOpenSettings: () => void;
  totalWordsCount: number;
}

export const Navbar: React.FC<NavbarProps> = ({
  activeTab,
  onSelectTab,
  progress,
  onOpenSettings,
  totalWordsCount
}) => {
  return (
    <header className="sticky top-0 z-40 bg-slate-950/90 backdrop-blur-md border-b border-slate-800">
      <div className="max-w-7xl mx-auto px-4 sm:px-6">
        {/* Main Row */}
        <div className="flex items-center justify-between h-16 gap-3">
          {/* Logo & Brand */}
          <div 
            onClick={() => onSelectTab('quiz_mixed')}
            className="flex items-center gap-2.5 cursor-pointer select-none group"
          >
            <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-emerald-600 to-teal-400 flex items-center justify-center text-white shadow-lg shadow-emerald-950/40 group-hover:scale-105 transition-transform">
              <Sparkles className="w-5 h-5" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="font-black text-lg sm:text-xl tracking-tight text-white">
                  Vocab<span className="text-emerald-400">Master</span>
                </span>
                <span className="hidden sm:inline-block px-2 py-0.5 text-[10px] font-bold rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">
                  {totalWordsCount} Palabras
                </span>
              </div>
              <p className="text-[10px] text-slate-400 hidden sm:block">
                Aprende inglés con audio e imágenes reales
              </p>
            </div>
          </div>

          {/* Desktop Navigation Links */}
          <nav className="hidden md:flex items-center gap-1 bg-slate-900/90 p-1 rounded-2xl border border-slate-800">
            <button
              onClick={() => onSelectTab('quiz_listen')}
              className={`flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-bold transition-all cursor-pointer ${
                activeTab === 'quiz_listen'
                  ? 'bg-emerald-500 text-white shadow-sm'
                  : 'text-slate-400 hover:text-white hover:bg-slate-800/80'
              }`}
            >
              <span>🎧 Escuchar</span>
            </button>

            <button
              onClick={() => onSelectTab('quiz_visual')}
              className={`flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-bold transition-all cursor-pointer ${
                activeTab === 'quiz_visual'
                  ? 'bg-emerald-500 text-white shadow-sm'
                  : 'text-slate-400 hover:text-white hover:bg-slate-800/80'
              }`}
            >
              <span>🖼️ Imagen</span>
            </button>

            <button
              onClick={() => onSelectTab('quiz_mixed')}
              className={`flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-bold transition-all cursor-pointer ${
                activeTab === 'quiz_mixed'
                  ? 'bg-emerald-500 text-white shadow-sm'
                  : 'text-slate-400 hover:text-white hover:bg-slate-800/80'
              }`}
            >
              <span>⚡ Reto Mixto</span>
            </button>

            <button
              onClick={() => onSelectTab('flashcards')}
              className={`flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-bold transition-all cursor-pointer ${
                activeTab === 'flashcards'
                  ? 'bg-emerald-500 text-white shadow-sm'
                  : 'text-slate-400 hover:text-white hover:bg-slate-800/80'
              }`}
            >
              <Layers className="w-3.5 h-3.5" />
              <span>Tarjetas</span>
            </button>

            <button
              onClick={() => onSelectTab('spelling')}
              className={`flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-bold transition-all cursor-pointer ${
                activeTab === 'spelling'
                  ? 'bg-emerald-500 text-white shadow-sm'
                  : 'text-slate-400 hover:text-white hover:bg-slate-800/80'
              }`}
            >
              <SpellCheck className="w-3.5 h-3.5" />
              <span>Deletreo</span>
            </button>

            <button
              onClick={() => onSelectTab('dictionary')}
              className={`flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-bold transition-all cursor-pointer ${
                activeTab === 'dictionary'
                  ? 'bg-emerald-500 text-white shadow-sm'
                  : 'text-slate-400 hover:text-white hover:bg-slate-800/80'
              }`}
            >
              <BookOpen className="w-3.5 h-3.5" />
              <span>Diccionario</span>
            </button>
          </nav>

          {/* Right: Streak, Score & Settings button */}
          <div className="flex items-center gap-2 sm:gap-3">
            {/* Streak */}
            <div className="flex items-center gap-1 px-2.5 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-amber-400 text-xs font-bold">
              <Flame className="w-4 h-4 text-amber-500" />
              <span>{progress.streak}</span>
            </div>

            {/* Score */}
            <div className="flex items-center gap-1 px-2.5 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-emerald-400 text-xs font-bold">
              <Trophy className="w-4 h-4 text-emerald-500" />
              <span>{progress.score}</span>
            </div>

            {/* Stats Tab Button */}
            <button
              onClick={() => onSelectTab('stats')}
              type="button"
              className={`p-2 rounded-xl border transition-colors cursor-pointer ${
                activeTab === 'stats'
                  ? 'bg-emerald-500 text-white border-emerald-400'
                  : 'bg-slate-900 text-slate-300 border-slate-800 hover:text-white'
              }`}
              title="Estadísticas"
            >
              <BarChart2 className="w-4 h-4" />
            </button>

            {/* Settings button */}
            <button
              onClick={onOpenSettings}
              type="button"
              className="p-2 rounded-xl bg-slate-900 border border-slate-800 text-slate-300 hover:text-white hover:border-slate-700 cursor-pointer transition-colors"
              title="Configuración de Audio y Acentos"
            >
              <Settings className="w-4 h-4" />
            </button>
          </div>
        </div>

        {/* Mobile Horizontal Subnav */}
        <div className="md:hidden flex items-center gap-1 overflow-x-auto py-2 border-t border-slate-900/60 scrollbar-none">
          <button
            onClick={() => onSelectTab('quiz_listen')}
            className={`px-3 py-1 rounded-lg text-xs font-bold whitespace-nowrap shrink-0 ${
              activeTab === 'quiz_listen' ? 'bg-emerald-500 text-white' : 'text-slate-400 bg-slate-900'
            }`}
          >
            🎧 Escuchar
          </button>
          <button
            onClick={() => onSelectTab('quiz_visual')}
            className={`px-3 py-1 rounded-lg text-xs font-bold whitespace-nowrap shrink-0 ${
              activeTab === 'quiz_visual' ? 'bg-emerald-500 text-white' : 'text-slate-400 bg-slate-900'
            }`}
          >
            🖼️ Imagen
          </button>
          <button
            onClick={() => onSelectTab('quiz_mixed')}
            className={`px-3 py-1 rounded-lg text-xs font-bold whitespace-nowrap shrink-0 ${
              activeTab === 'quiz_mixed' ? 'bg-emerald-500 text-white' : 'text-slate-400 bg-slate-900'
            }`}
          >
            ⚡ Mixto
          </button>
          <button
            onClick={() => onSelectTab('flashcards')}
            className={`px-3 py-1 rounded-lg text-xs font-bold whitespace-nowrap shrink-0 ${
              activeTab === 'flashcards' ? 'bg-emerald-500 text-white' : 'text-slate-400 bg-slate-900'
            }`}
          >
            🃏 Tarjetas
          </button>
          <button
            onClick={() => onSelectTab('spelling')}
            className={`px-3 py-1 rounded-lg text-xs font-bold whitespace-nowrap shrink-0 ${
              activeTab === 'spelling' ? 'bg-emerald-500 text-white' : 'text-slate-400 bg-slate-900'
            }`}
          >
            ✍️ Deletreo
          </button>
          <button
            onClick={() => onSelectTab('dictionary')}
            className={`px-3 py-1 rounded-lg text-xs font-bold whitespace-nowrap shrink-0 ${
              activeTab === 'dictionary' ? 'bg-emerald-500 text-white' : 'text-slate-400 bg-slate-900'
            }`}
          >
            📖 Diccionario ({totalWordsCount})
          </button>
        </div>
      </div>
    </header>
  );
};

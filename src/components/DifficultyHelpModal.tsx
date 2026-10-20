import React from 'react';
import { CEFRLevel } from '../types';
import { 
  X, 
  HelpCircle, 
  TrendingUp, 
  Zap, 
  Clock, 
  Award, 
  BookOpen, 
  Volume2, 
  SpellCheck,
  CheckCircle2,
  Gauge,
  Sliders,
  Sparkles
} from 'lucide-react';

interface DifficultyHelpModalProps {
  isOpen: boolean;
  onClose: () => void;
  totalWordsCount: number;
  levelCounts: Record<string, number>;
  selectedLevel: CEFRLevel | 'all';
  onSelectLevel: (lvl: CEFRLevel | 'all') => void;
  quizDifficulty: 'normal' | 'hard' | 'expert';
  onSelectQuizDifficulty: (diff: 'normal' | 'hard' | 'expert') => void;
}

export const DifficultyHelpModal: React.FC<DifficultyHelpModalProps> = ({
  isOpen,
  onClose,
  totalWordsCount,
  levelCounts,
  selectedLevel,
  onSelectLevel,
  quizDifficulty,
  onSelectQuizDifficulty
}) => {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black/80 backdrop-blur-sm flex items-center justify-center p-4 z-50 animate-in fade-in">
      <div className="bg-slate-900 border border-slate-800 rounded-3xl max-w-2xl w-full p-6 sm:p-8 flex flex-col gap-6 shadow-2xl relative max-h-[90vh] overflow-y-auto">
        
        {/* Header */}
        <div className="flex items-center justify-between border-b border-slate-800 pb-4">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-emerald-500 to-teal-400 flex items-center justify-center text-white shadow-lg">
              <TrendingUp className="w-5 h-5" />
            </div>
            <div>
              <h3 className="text-xl font-bold text-white">Guía de Niveles & Dificultad</h3>
              <p className="text-xs text-slate-400">¿Cuántas palabras hay y cómo subir el nivel de desafío?</p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="p-1.5 rounded-full text-slate-400 hover:text-white hover:bg-slate-800 cursor-pointer transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Section 1: Word Count Breakdown */}
        <div className="flex flex-col gap-3">
          <div className="flex items-center justify-between">
            <h4 className="text-sm font-bold uppercase tracking-wider text-emerald-400 flex items-center gap-1.5">
              <BookOpen className="w-4 h-4" />
              <span>1. Total de Palabras: {totalWordsCount} Palabras Certificadas</span>
            </h4>
            <span className="text-xs text-slate-400 font-medium">Meta original superada (+2,000)</span>
          </div>
          <p className="text-xs text-slate-300 leading-relaxed">
            El juego cuenta con <strong>{totalWordsCount} palabras únicas</strong> con pronunciación nativa, ejemplos bilingües e ilustraciones temáticas, distribuidas en los 5 niveles del Marco Común Europeo (CEFR):
          </p>

          <div className="grid grid-cols-2 sm:grid-cols-5 gap-2 mt-1">
            {[
              { lvl: 'A1', name: 'Principiante', color: 'border-emerald-500/40 bg-emerald-500/10 text-emerald-300' },
              { lvl: 'A2', name: 'Básico', color: 'border-sky-500/40 bg-sky-500/10 text-sky-300' },
              { lvl: 'B1', name: 'Intermedio', color: 'border-yellow-500/40 bg-yellow-500/10 text-yellow-300' },
              { lvl: 'B2', name: 'Inter. Alto', color: 'border-orange-500/40 bg-orange-500/10 text-orange-300' },
              { lvl: 'C1', name: 'Avanzado', color: 'border-rose-500/40 bg-rose-500/10 text-rose-300' }
            ].map(({ lvl, name, color }) => {
              const isCurrent = selectedLevel === lvl;
              return (
                <button
                  key={lvl}
                  onClick={() => onSelectLevel(lvl as CEFRLevel)}
                  className={`p-2.5 rounded-xl border text-center transition-all cursor-pointer ${color} ${
                    isCurrent ? 'ring-2 ring-white font-black scale-102' : 'opacity-85 hover:opacity-100'
                  }`}
                >
                  <div className="text-xs font-black">{lvl}</div>
                  <div className="text-[10px] text-slate-300 mt-0.5">{name}</div>
                  <div className="text-[11px] font-bold text-white mt-1">
                    {levelCounts[lvl] || 0} palabras
                  </div>
                </button>
              );
            })}
          </div>
        </div>

        {/* Section 2: How to raise difficulty */}
        <div className="flex flex-col gap-3 pt-4 border-t border-slate-800">
          <h4 className="text-sm font-bold uppercase tracking-wider text-amber-400 flex items-center gap-1.5">
            <Sliders className="w-4 h-4" />
            <span>2. Formas de Subir el Nivel de Dificultad</span>
          </h4>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            {/* Strategy 1: CEFR Level */}
            <div className="bg-slate-800/60 border border-slate-700/60 rounded-2xl p-4 flex flex-col gap-1.5">
              <div className="flex items-center gap-2">
                <span className="w-6 h-6 rounded-lg bg-yellow-500/20 text-yellow-300 border border-yellow-500/30 flex items-center justify-center text-xs font-bold">1</span>
                <span className="font-bold text-sm text-white">Filtrar por Nivel CEFR</span>
              </div>
              <p className="text-xs text-slate-400">
                Selecciona <strong>B1, B2 o C1</strong> en la barra superior para practicar vocabulario formal, académico, modismos y phrasal verbs avanzados en lugar de palabras básicas.
              </p>
            </div>

            {/* Strategy 2: Quiz Options */}
            <div className="bg-slate-800/60 border border-slate-700/60 rounded-2xl p-4 flex flex-col gap-1.5">
              <div className="flex items-center gap-2">
                <span className="w-6 h-6 rounded-lg bg-orange-500/20 text-orange-300 border border-orange-500/30 flex items-center justify-center text-xs font-bold">2</span>
                <span className="font-bold text-sm text-white">Activar 6 Opciones (Difícil)</span>
              </div>
              <p className="text-xs text-slate-400">
                Cambia de 4 a <strong>6 opciones</strong> de respuesta en el Quiz. Los distractores pertenecen a la misma categoría, exigiendo discriminación visual y auditiva fina.
              </p>
            </div>

            {/* Strategy 3: Timer Expert */}
            <div className="bg-slate-800/60 border border-slate-700/60 rounded-2xl p-4 flex flex-col gap-1.5">
              <div className="flex items-center gap-2">
                <span className="w-6 h-6 rounded-lg bg-rose-500/20 text-rose-300 border border-rose-500/30 flex items-center justify-center text-xs font-bold">3</span>
                <span className="font-bold text-sm text-white">Modo Contrarreloj (Experto)</span>
              </div>
              <p className="text-xs text-slate-400">
                Activa el <strong>Modo Experto</strong> con cronómetro regresivo de 15 segundos por palabra para entrenar la respuesta instantánea bajo presión.
              </p>
            </div>

            {/* Strategy 4: Spelling Mode */}
            <div className="bg-slate-800/60 border border-slate-700/60 rounded-2xl p-4 flex flex-col gap-1.5">
              <div className="flex items-center gap-2">
                <span className="w-6 h-6 rounded-lg bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 flex items-center justify-center text-xs font-bold">4</span>
                <span className="font-bold text-sm text-white">Modo Deletreo (✍️)</span>
              </div>
              <p className="text-xs text-slate-400">
                Entra a la pestaña <strong>Deletreo</strong>. En este modo no hay opciones múltiples: debes construir o escribir letra por letra la palabra correcta en inglés.
              </p>
            </div>

            {/* Strategy 5: Reto Brutal */}
            <div className="bg-gradient-to-r from-rose-950/40 to-slate-800/60 border border-rose-500/30 rounded-2xl p-4 flex flex-col gap-1.5">
              <div className="flex items-center gap-2">
                <span className="w-6 h-6 rounded-lg bg-rose-500/20 text-rose-300 border border-rose-500/30 flex items-center justify-center text-xs font-bold">5</span>
                <span className="font-bold text-sm text-rose-300 flex items-center gap-1">
                  <span>💀 Reto Brutal (¡Nuevo!)</span>
                </span>
              </div>
              <p className="text-xs text-slate-300">
                El desafío definitivo de trampas: homófonos que suenan igual (<em>desert</em> vs <em>dessert</em>, <em>bear</em> vs <em>beard</em> vs <em>beer</em>), falsos amigos (<em>library</em> ≠ librería, <em>actually</em> ≠ actualmente) y homógrafos (<em>tear</em>, <em>lead</em>).
              </p>
            </div>
          </div>
        </div>

        {/* Section 3: Quick Difficulty Selector */}
        <div className="bg-slate-950/60 border border-slate-800 rounded-2xl p-4 flex flex-col gap-3">
          <label className="text-xs font-bold text-slate-300 flex items-center gap-1.5">
            <Zap className="w-4 h-4 text-amber-400" />
            <span>Configurar Dificultad del Quiz Ahora:</span>
          </label>
          <div className="grid grid-cols-3 gap-2">
            {[
              { id: 'normal', name: 'Normal', desc: '4 opciones estándar', icon: '⚡' },
              { id: 'hard', name: 'Difícil', desc: '6 opciones similares', icon: '🔥' },
              { id: 'expert', name: 'Experto', desc: '6 opciones + 15s', icon: '⏱️' }
            ].map((diff) => (
              <button
                key={diff.id}
                onClick={() => onSelectQuizDifficulty(diff.id as any)}
                className={`p-2.5 rounded-xl border text-center transition-all cursor-pointer ${
                  quizDifficulty === diff.id
                    ? 'bg-emerald-500/20 text-emerald-300 border-emerald-500 ring-2 ring-emerald-500/40'
                    : 'bg-slate-900 text-slate-300 border-slate-800 hover:border-slate-700'
                }`}
              >
                <div className="text-sm font-bold">{diff.icon} {diff.name}</div>
                <div className="text-[10px] text-slate-400 mt-0.5">{diff.desc}</div>
              </button>
            ))}
          </div>
        </div>

        {/* Close */}
        <button
          onClick={onClose}
          type="button"
          className="w-full py-3 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-sm cursor-pointer shadow-lg transition-colors"
        >
          ¡Entendido, vamos a jugar!
        </button>

      </div>
    </div>
  );
};

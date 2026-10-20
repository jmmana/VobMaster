import React from 'react';
import { WordItem, UserProgress } from '../types';
import { AudioPlayerButton } from './AudioPlayerButton';
import { 
  Trophy, 
  Flame, 
  Target, 
  BookOpen, 
  AlertCircle, 
  CheckCircle2, 
  RotateCcw,
  Sparkles
} from 'lucide-react';

interface StatsViewProps {
  progress: UserProgress;
  words: WordItem[];
  totalWordsCount: number;
  onClearMistakes: () => void;
  accent: 'US' | 'UK' | 'AU';
  rate: number;
}

export const StatsView: React.FC<StatsViewProps> = ({
  progress,
  words,
  totalWordsCount,
  onClearMistakes,
  accent,
  rate
}) => {
  const accuracy = progress.totalAnswered > 0
    ? Math.round((progress.correctAnswers / progress.totalAnswered) * 100)
    : 0;

  const masteredCount = progress.masteredWordIds.length;
  const progressPercent = Math.min(100, Math.round((masteredCount / totalWordsCount) * 100));

  // Find missed words items
  const mistakeWords = words.filter((w) => progress.mistakeWordIds.includes(w.id));

  return (
    <div className="max-w-4xl mx-auto px-4 py-8 flex flex-col gap-8">
      {/* Page Title */}
      <div>
        <h2 className="text-3xl font-extrabold text-white flex items-center gap-2.5">
          <Trophy className="w-8 h-8 text-amber-400" />
          <span>Tu Progreso & Estadísticas</span>
        </h2>
        <p className="text-slate-400 text-sm mt-1">
          Seguimiento de tu dominio sobre el banco de <strong>{totalWordsCount} palabras</strong> en inglés.
        </p>
      </div>

      {/* KPI Cards */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
        {/* Total Points */}
        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 flex flex-col gap-1">
          <div className="flex items-center justify-between text-slate-400 text-xs font-semibold">
            <span>PUNTOS TOTALES</span>
            <Trophy className="w-4 h-4 text-amber-400" />
          </div>
          <span className="text-2xl sm:text-3xl font-black text-white mt-1">
            {progress.score.toLocaleString()}
          </span>
          <span className="text-[11px] text-emerald-400">Puntaje acumulado</span>
        </div>

        {/* Accuracy */}
        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 flex flex-col gap-1">
          <div className="flex items-center justify-between text-slate-400 text-xs font-semibold">
            <span>PRECISIÓN</span>
            <Target className="w-4 h-4 text-emerald-400" />
          </div>
          <span className="text-2xl sm:text-3xl font-black text-white mt-1">
            {accuracy}%
          </span>
          <span className="text-[11px] text-slate-400">
            {progress.correctAnswers} de {progress.totalAnswered} aciertos
          </span>
        </div>

        {/* Best Streak */}
        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 flex flex-col gap-1">
          <div className="flex items-center justify-between text-slate-400 text-xs font-semibold">
            <span>MEJOR RACHA</span>
            <Flame className="w-4 h-4 text-orange-400" />
          </div>
          <span className="text-2xl sm:text-3xl font-black text-white mt-1">
            {progress.bestStreak}
          </span>
          <span className="text-[11px] text-amber-400">Racha actual: {progress.streak}</span>
        </div>

        {/* Words Mastered */}
        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 flex flex-col gap-1">
          <div className="flex items-center justify-between text-slate-400 text-xs font-semibold">
            <span>DOMINADAS</span>
            <BookOpen className="w-4 h-4 text-sky-400" />
          </div>
          <span className="text-2xl sm:text-3xl font-black text-white mt-1">
            {masteredCount}
          </span>
          <span className="text-[11px] text-sky-400">de {totalWordsCount} palabras</span>
        </div>
      </div>

      {/* Mastery Progress Bar */}
      <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6 flex flex-col gap-3">
        <div className="flex items-center justify-between">
          <div>
            <h3 className="font-bold text-white text-base">Meta de Dominio del Diccionario</h3>
            <p className="text-xs text-slate-400">
              Has dominado <strong>{masteredCount}</strong> de {totalWordsCount} palabras
            </p>
          </div>
          <span className="text-xl font-extrabold text-emerald-400">{progressPercent}%</span>
        </div>

        <div className="w-full h-3.5 rounded-full bg-slate-800 overflow-hidden relative">
          <div
            className="h-full bg-gradient-to-r from-emerald-500 to-teal-400 rounded-full transition-all duration-500"
            style={{ width: `${Math.max(2, progressPercent)}%` }}
          />
        </div>
      </div>

      {/* Level Breakdown Progress Card */}
      <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6 flex flex-col gap-4">
        <div>
          <h3 className="font-bold text-white text-base">Progreso por Nivel de Dificultad (CEFR)</h3>
          <p className="text-xs text-slate-400">
            Monitorea tu aprendizaje a medida que avanzas hacia niveles más complejos.
          </p>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-5 gap-3">
          {(['A1', 'A2', 'B1', 'B2', 'C1'] as const).map((lvl) => {
            const levelTotal = words.filter((w) => w.level === lvl).length;
            const levelMastered = words.filter(
              (w) => w.level === lvl && progress.masteredWordIds.includes(w.id)
            ).length;
            const pct = levelTotal > 0 ? Math.round((levelMastered / levelTotal) * 100) : 0;

            const badgeColor = 
              lvl === 'A1' ? 'border-emerald-500/30 bg-emerald-500/10 text-emerald-300' :
              lvl === 'A2' ? 'border-sky-500/30 bg-sky-500/10 text-sky-300' :
              lvl === 'B1' ? 'border-yellow-500/30 bg-yellow-500/10 text-yellow-300' :
              lvl === 'B2' ? 'border-orange-500/30 bg-orange-500/10 text-orange-300' :
              'border-rose-500/30 bg-rose-500/10 text-rose-300';

            const barColor =
              lvl === 'A1' ? 'bg-emerald-500' :
              lvl === 'A2' ? 'bg-sky-500' :
              lvl === 'B1' ? 'bg-yellow-500' :
              lvl === 'B2' ? 'bg-orange-500' :
              'bg-rose-500';

            return (
              <div
                key={lvl}
                className="bg-slate-800/60 border border-slate-700/60 rounded-2xl p-3.5 flex flex-col justify-between gap-2"
              >
                <div className="flex items-center justify-between">
                  <span className={`px-2 py-0.5 rounded-lg text-xs font-black border ${badgeColor}`}>
                    {lvl}
                  </span>
                  <span className="text-xs font-bold text-slate-300">{pct}%</span>
                </div>

                <div>
                  <div className="text-xs font-bold text-white">
                    {levelMastered} <span className="text-slate-400 font-normal">/ {levelTotal}</span>
                  </div>
                  <div className="text-[10px] text-slate-400">
                    {lvl === 'A1' ? 'Principiante' : lvl === 'A2' ? 'Básico' : lvl === 'B1' ? 'Intermedio' : lvl === 'B2' ? 'Inter. Alto' : 'Avanzado'}
                  </div>
                </div>

                <div className="w-full h-1.5 rounded-full bg-slate-700/60 overflow-hidden">
                  <div
                    className={`h-full ${barColor} rounded-full transition-all duration-500`}
                    style={{ width: `${Math.max(2, pct)}%` }}
                  />
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Review Queue (Mistakes to Review) */}
      <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6 flex flex-col gap-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2.5">
            <AlertCircle className="w-5 h-5 text-amber-400" />
            <h3 className="font-bold text-white text-base">
              Palabras para Repasar ({mistakeWords.length})
            </h3>
          </div>

          {mistakeWords.length > 0 && (
            <button
              onClick={onClearMistakes}
              type="button"
              className="text-xs text-slate-400 hover:text-white underline cursor-pointer"
            >
              Limpiar lista
            </button>
          )}
        </div>

        {mistakeWords.length === 0 ? (
          <div className="text-center py-8 text-slate-500 text-sm">
            ¡Excelente! No tienes palabras pendientes de repasar.
          </div>
        ) : (
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            {mistakeWords.map((word) => (
              <div
                key={word.id}
                className="bg-slate-800/60 rounded-xl p-3.5 border border-slate-800 flex items-center justify-between gap-3"
              >
                <div>
                  <div className="flex items-center gap-2">
                    <span className="text-base">{word.emoji}</span>
                    <strong className="text-white capitalize">{word.word}</strong>
                    <span className="text-xs text-slate-400">({word.phonetic})</span>
                  </div>
                  <p className="text-xs text-emerald-400 font-medium capitalize mt-0.5">
                    {word.translation}
                  </p>
                </div>

                <AudioPlayerButton
                  text={word.word}
                  size="sm"
                  accent={accent}
                  rate={rate}
                />
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

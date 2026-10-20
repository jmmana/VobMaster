/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useState, useEffect, useMemo } from 'react';
import { words } from './data/words';
import { categories } from './data/categories';
import { GameSettings, UserProgress, CEFRLevel } from './types';
import { Navbar, ActiveTab } from './components/Navbar';
import { QuizView } from './components/QuizView';
import { FlashcardsView } from './components/FlashcardsView';
import { SpellingView } from './components/SpellingView';
import { BrutalChallengeView } from './components/BrutalChallengeView';
import { DictionaryView } from './components/DictionaryView';
import { StatsView } from './components/StatsView';
import { SettingsModal } from './components/SettingsModal';
import { DifficultyHelpModal } from './components/DifficultyHelpModal';
import { audioService } from './services/audioService';
import { 
  Volume2, 
  Eye, 
  Sparkles, 
  Layers, 
  SpellCheck, 
  BookOpen, 
  BarChart2, 
  Play, 
  Flame,
  Award,
  CheckCircle2,
  Filter
} from 'lucide-react';

const STORAGE_KEY_PROGRESS = 'vocabmaster_user_progress_v2';
const STORAGE_KEY_SETTINGS = 'vocabmaster_user_settings_v2';

const defaultSettings: GameSettings = {
  speechRate: 0.95,
  voiceAccent: 'US',
  autoPlayAudio: true,
  soundEffects: true,
  selectedCategory: 'all',
  selectedLevel: 'all',
  questionsPerRound: 10,
  quizDifficulty: 'normal',
  timerSeconds: 15
};

const defaultProgress: UserProgress = {
  score: 0,
  streak: 0,
  bestStreak: 0,
  totalAnswered: 0,
  correctAnswers: 0,
  masteredWordIds: [],
  favoriteWordIds: [],
  mistakeWordIds: [],
  levelProgress: {
    A1: { answered: 0, correct: 0 },
    A2: { answered: 0, correct: 0 },
    B1: { answered: 0, correct: 0 },
    B2: { answered: 0, correct: 0 },
    C1: { answered: 0, correct: 0 }
  }
};

export default function App() {
  const [settings, setSettings] = useState<GameSettings>(() => {
    try {
      const saved = localStorage.getItem(STORAGE_KEY_SETTINGS);
      return saved ? { ...defaultSettings, ...JSON.parse(saved) } : defaultSettings;
    } catch {
      return defaultSettings;
    }
  });

  const [progress, setProgress] = useState<UserProgress>(() => {
    try {
      const saved = localStorage.getItem(STORAGE_KEY_PROGRESS);
      return saved ? JSON.parse(saved) : defaultProgress;
    } catch {
      return defaultProgress;
    }
  });

  const [activeTab, setActiveTab] = useState<ActiveTab>('quiz_mixed');
  const [isSettingsOpen, setIsSettingsOpen] = useState(false);
  const [isDifficultyHelpOpen, setIsDifficultyHelpOpen] = useState(false);

  // Precompute word counts per CEFR level
  const levelCounts = useMemo(() => {
    const counts: Record<string, number> = { A1: 0, A2: 0, B1: 0, B2: 0, C1: 0 };
    words.forEach((w) => {
      if (counts[w.level] !== undefined) {
        counts[w.level]++;
      }
    });
    return counts;
  }, []);

  // Sync settings to localStorage
  useEffect(() => {
    try {
      localStorage.setItem(STORAGE_KEY_SETTINGS, JSON.stringify(settings));
    } catch {
      // ignore
    }
  }, [settings]);

  // Sync progress to localStorage
  useEffect(() => {
    try {
      localStorage.setItem(STORAGE_KEY_PROGRESS, JSON.stringify(progress));
    } catch {
      // ignore
    }
  }, [progress]);

  const handleToggleFavorite = (wordId: number) => {
    audioService.playClickSound();
    setProgress((prev) => {
      const isFav = prev.favoriteWordIds.includes(wordId);
      return {
        ...prev,
        favoriteWordIds: isFav
          ? prev.favoriteWordIds.filter((id) => id !== wordId)
          : [...prev.favoriteWordIds, wordId]
      };
    });
  };

  const handleClearMistakes = () => {
    audioService.playClickSound();
    setProgress((prev) => ({
      ...prev,
      mistakeWordIds: []
    }));
  };

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex flex-col font-sans selection:bg-emerald-500 selection:text-white">
      {/* Top Navigation */}
      <Navbar
        activeTab={activeTab}
        onSelectTab={setActiveTab}
        progress={progress}
        onOpenSettings={() => setIsSettingsOpen(true)}
        totalWordsCount={words.length}
      />

      {/* Mode Quick Select / Filter & Difficulty Banner */}
      <div className="bg-slate-900/80 border-b border-slate-800/80 px-4 py-2.5">
        <div className="max-w-7xl mx-auto flex flex-col gap-2.5">
          {/* Top Row: Active Mode & How to Raise Difficulty Help Button */}
          <div className="flex flex-wrap items-center justify-between gap-3 text-xs">
            <div className="flex items-center gap-2">
              <span className="font-semibold text-slate-300">Modo actual:</span>
              <span className="px-2.5 py-0.5 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-bold capitalize">
                {activeTab === 'quiz_listen' && '🎧 Escuchar y Seleccionar'}
                {activeTab === 'quiz_visual' && '🖼️ Mirar Imagen y Seleccionar'}
                {activeTab === 'quiz_mixed' && '⚡ Reto Mixto (Audio + Imagen)'}
                {activeTab === 'quiz_brutal' && '💀 Reto Brutal: Homófonos, Falsos Amigos & Trampas'}
                {activeTab === 'flashcards' && '🃏 Tarjetas de Estudio'}
                {activeTab === 'spelling' && '✍️ Deletreo y Constructor'}
                {activeTab === 'dictionary' && `📖 Diccionario (${words.length} Palabras)`}
                {activeTab === 'stats' && '📊 Progreso y Resumen'}
              </span>
            </div>

            {/* Quick Actions */}
            <div className="flex items-center gap-2">
              {/* Category dropdown */}
              <select
                value={settings.selectedCategory}
                onChange={(e) =>
                  setSettings((prev) => ({ ...prev, selectedCategory: e.target.value }))
                }
                className="bg-slate-800 border border-slate-700 text-slate-200 rounded-lg px-2.5 py-1 text-xs cursor-pointer focus:outline-none focus:ring-1 focus:ring-emerald-500"
              >
                <option value="all">Todas las categorías ({words.length})</option>
                {categories.map((c) => (
                  <option key={c.id} value={c.id}>
                    {c.emoji} {c.name} ({c.count})
                  </option>
                ))}
              </select>

              {/* How to raise difficulty guide button */}
              <button
                type="button"
                onClick={() => setIsDifficultyHelpOpen(true)}
                className="px-2.5 py-1 rounded-lg bg-amber-500/15 hover:bg-amber-500/25 text-amber-300 border border-amber-500/30 font-bold text-xs flex items-center gap-1.5 transition-colors cursor-pointer shadow-sm"
                title="Información sobre cantidad de palabras y cómo subir dificultad"
              >
                <span>💡 ¿Cómo subir dificultad?</span>
              </button>
            </div>
          </div>

          {/* Bottom Row: Direct Level Selector & Quiz Challenge Mode Pills */}
          <div className="flex flex-wrap items-center justify-between gap-2.5 pt-2 border-t border-slate-800/60 text-xs">
            {/* CEFR Level Pills */}
            <div className="flex items-center gap-1.5 flex-wrap">
              <span className="text-slate-400 font-semibold mr-1">Nivel:</span>
              <button
                type="button"
                onClick={() => setSettings((prev) => ({ ...prev, selectedLevel: 'all' }))}
                className={`px-2.5 py-1 rounded-lg font-bold text-xs transition-all cursor-pointer ${
                  settings.selectedLevel === 'all'
                    ? 'bg-emerald-500 text-white shadow-sm'
                    : 'bg-slate-800/80 text-slate-400 hover:text-slate-200'
                }`}
              >
                Todos ({words.length})
              </button>

              {(['A1', 'A2', 'B1', 'B2', 'C1'] as const).map((lvl) => {
                const isSelected = settings.selectedLevel === lvl;
                const badgeColor = 
                  lvl === 'A1' ? 'border-emerald-500/40 text-emerald-300' :
                  lvl === 'A2' ? 'border-sky-500/40 text-sky-300' :
                  lvl === 'B1' ? 'border-yellow-500/40 text-yellow-300' :
                  lvl === 'B2' ? 'border-orange-500/40 text-orange-300' :
                  'border-rose-500/40 text-rose-300';

                return (
                  <button
                    key={lvl}
                    type="button"
                    onClick={() => setSettings((prev) => ({ ...prev, selectedLevel: lvl }))}
                    className={`px-2 py-1 rounded-lg font-bold text-xs border transition-all cursor-pointer ${
                      isSelected
                        ? 'bg-slate-100 text-slate-950 border-white shadow-md font-black'
                        : `bg-slate-800/80 hover:bg-slate-700/80 ${badgeColor}`
                    }`}
                  >
                    {lvl} ({levelCounts[lvl] || 0})
                  </button>
                );
              })}
            </div>

            {/* Quiz Challenge Difficulty Pills */}
            <div className="flex items-center gap-1.5 flex-wrap">
              <span className="text-slate-400 font-semibold mr-1">Reto:</span>
              <button
                type="button"
                onClick={() => setSettings((prev) => ({ ...prev, quizDifficulty: 'normal' }))}
                className={`px-2.5 py-1 rounded-lg font-bold text-xs transition-all cursor-pointer ${
                  settings.quizDifficulty === 'normal'
                    ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/40'
                    : 'bg-slate-800/80 text-slate-400 hover:text-slate-200'
                }`}
              >
                ⚡ 4 Opciones
              </button>

              <button
                type="button"
                onClick={() => setSettings((prev) => ({ ...prev, quizDifficulty: 'hard' }))}
                className={`px-2.5 py-1 rounded-lg font-bold text-xs transition-all cursor-pointer ${
                  settings.quizDifficulty === 'hard'
                    ? 'bg-amber-500/20 text-amber-300 border border-amber-500/40'
                    : 'bg-slate-800/80 text-slate-400 hover:text-slate-200'
                }`}
              >
                🔥 6 Opc (Difícil)
              </button>

              <button
                type="button"
                onClick={() => setSettings((prev) => ({ ...prev, quizDifficulty: 'expert' }))}
                className={`px-2.5 py-1 rounded-lg font-bold text-xs transition-all cursor-pointer ${
                  settings.quizDifficulty === 'expert'
                    ? 'bg-rose-500/20 text-rose-300 border border-rose-500/40'
                    : 'bg-slate-800/80 text-slate-400 hover:text-slate-200'
                }`}
              >
                ⏱️ 15s (Experto)
              </button>
            </div>
          </div>
        </div>
      </div>

      {/* Main View Container */}
      <main className="flex-1 w-full">
        {activeTab === 'quiz_listen' && (
          <QuizView
            words={words}
            settings={settings}
            progress={progress}
            onUpdateProgress={setProgress}
            mode="listen"
            onExit={() => setActiveTab('quiz_mixed')}
          />
        )}

        {activeTab === 'quiz_visual' && (
          <QuizView
            words={words}
            settings={settings}
            progress={progress}
            onUpdateProgress={setProgress}
            mode="visual"
            onExit={() => setActiveTab('quiz_mixed')}
          />
        )}

        {activeTab === 'quiz_mixed' && (
          <QuizView
            words={words}
            settings={settings}
            progress={progress}
            onUpdateProgress={setProgress}
            mode="mixed"
            onExit={() => setActiveTab('dictionary')}
          />
        )}

        {activeTab === 'quiz_brutal' && (
          <BrutalChallengeView
            settings={settings}
            progress={progress}
            onUpdateProgress={setProgress}
            onExit={() => setActiveTab('quiz_mixed')}
          />
        )}

        {activeTab === 'flashcards' && (
          <FlashcardsView
            words={words}
            settings={settings}
            progress={progress}
            onUpdateProgress={setProgress}
          />
        )}

        {activeTab === 'spelling' && (
          <SpellingView
            words={words}
            settings={settings}
            progress={progress}
            onUpdateProgress={setProgress}
          />
        )}

        {activeTab === 'dictionary' && (
          <DictionaryView
            words={words}
            categories={categories}
            progress={progress}
            onToggleFavorite={handleToggleFavorite}
            accent={settings.voiceAccent}
            rate={settings.speechRate}
          />
        )}

        {activeTab === 'stats' && (
          <StatsView
            progress={progress}
            words={words}
            totalWordsCount={words.length}
            onClearMistakes={handleClearMistakes}
            accent={settings.voiceAccent}
            rate={settings.speechRate}
          />
        )}
      </main>

      {/* Settings Modal */}
      <SettingsModal
        isOpen={isSettingsOpen}
        onClose={() => setIsSettingsOpen(false)}
        settings={settings}
        onUpdateSettings={setSettings}
        categories={categories}
      />

      {/* Difficulty & Word Count Help Modal */}
      <DifficultyHelpModal
        isOpen={isDifficultyHelpOpen}
        onClose={() => setIsDifficultyHelpOpen(false)}
        totalWordsCount={words.length}
        levelCounts={levelCounts}
        selectedLevel={settings.selectedLevel}
        onSelectLevel={(lvl) => setSettings((prev) => ({ ...prev, selectedLevel: lvl }))}
        quizDifficulty={settings.quizDifficulty}
        onSelectQuizDifficulty={(diff) => setSettings((prev) => ({ ...prev, quizDifficulty: diff }))}
      />

      {/* Footer */}
      <footer className="border-t border-slate-900 bg-slate-950/80 py-4 px-4 text-center text-xs text-slate-500">
        <div className="max-w-6xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-2">
          <span>VocabMaster &bull; Banco certificado de <strong>{words.length} palabras</strong> en inglés con pronunciación nativa e imágenes interactivas.</span>
          <div className="flex items-center gap-3">
            <span>Acento: <strong>{settings.voiceAccent === 'US' ? 'Americano' : settings.voiceAccent === 'UK' ? 'Británico' : 'Australiano'}</strong></span>
            <span>&bull;</span>
            <span>Velocidad: <strong>{settings.speechRate}x</strong></span>
          </div>
        </div>
      </footer>
    </div>
  );
}

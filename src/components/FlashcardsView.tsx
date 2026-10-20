import React, { useState, useEffect } from 'react';
import confetti from 'canvas-confetti';
import { WordItem, UserProgress, GameSettings } from '../types';
import { WordIllustration } from './WordIllustration';
import { AudioPlayerButton } from './AudioPlayerButton';
import { audioService } from '../services/audioService';
import { 
  RotateCw, 
  ChevronLeft, 
  ChevronRight, 
  Check, 
  X, 
  Shuffle, 
  Sparkles,
  Volume2,
  Bookmark
} from 'lucide-react';

interface FlashcardsViewProps {
  words: WordItem[];
  settings: GameSettings;
  progress: UserProgress;
  onUpdateProgress: (updater: (prev: UserProgress) => UserProgress) => void;
}

export const FlashcardsView: React.FC<FlashcardsViewProps> = ({
  words,
  settings,
  progress,
  onUpdateProgress
}) => {
  const [deck, setDeck] = useState<WordItem[]>([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isFlipped, setIsFlipped] = useState(false);

  // Initialize deck based on category or mistake queue
  useEffect(() => {
    let pool = words;
    if (settings.selectedCategory !== 'all') {
      pool = pool.filter((w) => w.categoryId === settings.selectedCategory);
    }
    if (settings.selectedLevel !== 'all') {
      pool = pool.filter((w) => w.level === settings.selectedLevel);
    }
    setDeck(pool.length > 0 ? pool : words);
    setCurrentIndex(0);
    setIsFlipped(false);
  }, [words, settings.selectedCategory, settings.selectedLevel]);

  const currentWord = deck[currentIndex];

  const handleFlip = () => {
    audioService.playClickSound();
    setIsFlipped(!isFlipped);
  };

  const handleNext = () => {
    audioService.playClickSound();
    setIsFlipped(false);
    setCurrentIndex((prev) => (prev + 1) % deck.length);
  };

  const handlePrev = () => {
    audioService.playClickSound();
    setIsFlipped(false);
    setCurrentIndex((prev) => (prev - 1 + deck.length) % deck.length);
  };

  const handleShuffle = () => {
    audioService.playClickSound();
    setDeck([...deck].sort(() => 0.5 - Math.random()));
    setCurrentIndex(0);
    setIsFlipped(false);
  };

  const markMastered = () => {
    if (!currentWord) return;
    audioService.playCorrectSound();
    confetti({ particleCount: 30, spread: 50 });

    onUpdateProgress((prev) => ({
      ...prev,
      masteredWordIds: prev.masteredWordIds.includes(currentWord.id)
        ? prev.masteredWordIds
        : [...prev.masteredWordIds, currentWord.id]
    }));
    handleNext();
  };

  const markReview = () => {
    if (!currentWord) return;
    audioService.playWrongSound();

    onUpdateProgress((prev) => ({
      ...prev,
      mistakeWordIds: prev.mistakeWordIds.includes(currentWord.id)
        ? prev.mistakeWordIds
        : [...prev.mistakeWordIds, currentWord.id]
    }));
    handleNext();
  };

  if (!currentWord) {
    return (
      <div className="text-center py-16 text-slate-400">
        Cargando tarjetas...
      </div>
    );
  }

  return (
    <div className="max-w-xl mx-auto px-4 py-8 flex flex-col items-center gap-6">
      {/* Top Deck Info */}
      <div className="w-full flex items-center justify-between text-xs text-slate-400 px-2">
        <span>
          Tarjeta <strong>{currentIndex + 1}</strong> de {deck.length}
        </span>
        <button
          onClick={handleShuffle}
          type="button"
          className="flex items-center gap-1.5 px-3 py-1 rounded-full bg-slate-800 text-slate-300 hover:text-white border border-slate-700 cursor-pointer"
        >
          <Shuffle className="w-3.5 h-3.5" />
          <span>Barajar</span>
        </button>
      </div>

      {/* 3D Flashcard Container */}
      <div
        onClick={handleFlip}
        className="w-full h-96 sm:h-[420px] rounded-3xl bg-slate-900 border border-slate-800 p-6 sm:p-8 flex flex-col justify-between cursor-pointer hover:border-slate-700 transition-all shadow-2xl relative select-none group"
      >
        {!isFlipped ? (
          /* FRONT SIDE: Image, English Word & Audio */
          <div className="flex flex-col items-center justify-between h-full">
            <div className="flex items-center justify-between w-full">
              <span className="px-3 py-1 text-xs font-bold rounded-full bg-slate-800 text-slate-300 border border-slate-700 uppercase">
                {currentWord.level}
              </span>
              <span className="text-xs text-slate-400 font-medium">
                {currentWord.category}
              </span>
            </div>

            {/* Central Visual Scene */}
            <div className="w-full max-w-[220px]">
              <WordIllustration word={currentWord} size="md" showDetails={false} />
            </div>

            <div className="text-center">
              <h2 className="text-3xl sm:text-4xl font-extrabold text-white capitalize tracking-wide">
                {currentWord.word}
              </h2>
              <p className="text-emerald-400 font-mono text-sm mt-1">
                {currentWord.phonetic}
              </p>
            </div>

            <div className="flex items-center gap-2">
              <AudioPlayerButton
                text={currentWord.word}
                size="md"
                accent={settings.voiceAccent}
                rate={settings.speechRate}
                label="Pronunciar"
              />
            </div>

            <p className="text-xs text-slate-500 flex items-center gap-1.5">
              <RotateCw className="w-3.5 h-3.5" />
              <span>Haz clic en la tarjeta para voltear y ver traducción</span>
            </p>
          </div>
        ) : (
          /* BACK SIDE: Spanish Translation, Sentence & Details */
          <div className="flex flex-col items-center justify-between h-full text-center">
            <div className="w-full flex items-center justify-between">
              <span className="text-xs text-emerald-400 font-bold uppercase tracking-wider">
                Traducción & Contexto
              </span>
              <span className="text-xs text-slate-400">
                {currentWord.emoji} {currentWord.word}
              </span>
            </div>

            <div className="my-auto flex flex-col items-center gap-3">
              <span className="text-4xl font-black text-emerald-400 capitalize">
                {currentWord.translation}
              </span>

              <div className="bg-slate-800/60 p-4 rounded-2xl border border-slate-800 max-w-md text-left mt-2">
                <div className="flex items-center justify-between mb-1">
                  <span className="text-xs font-bold text-slate-400">Frase de ejemplo:</span>
                  <AudioPlayerButton
                    text={currentWord.example}
                    size="sm"
                    accent={settings.voiceAccent}
                    rate={0.9}
                  />
                </div>
                <p className="text-white text-sm font-medium italic">"{currentWord.example}"</p>
                <p className="text-slate-400 text-xs mt-1">{currentWord.exampleEs}</p>
              </div>
            </div>

            <p className="text-xs text-slate-500 flex items-center gap-1.5">
              <RotateCw className="w-3.5 h-3.5" />
              <span>Haz clic para regresar al frente</span>
            </p>
          </div>
        )}
      </div>

      {/* Action Buttons: Still learning vs Mastered */}
      <div className="w-full flex items-center justify-between gap-4">
        <button
          onClick={handlePrev}
          type="button"
          className="p-3 rounded-2xl bg-slate-900 border border-slate-800 hover:bg-slate-800 text-slate-300 cursor-pointer"
          title="Anterior"
        >
          <ChevronLeft className="w-5 h-5" />
        </button>

        <button
          onClick={markReview}
          type="button"
          className="flex-1 py-3 px-4 rounded-2xl bg-rose-950/40 border border-rose-800/60 hover:bg-rose-900/50 text-rose-300 font-bold text-sm flex items-center justify-center gap-2 cursor-pointer transition-colors"
        >
          <X className="w-4 h-4" />
          <span>Repasar luego</span>
        </button>

        <button
          onClick={markMastered}
          type="button"
          className="flex-1 py-3 px-4 rounded-2xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-sm flex items-center justify-center gap-2 shadow-lg shadow-emerald-950/40 cursor-pointer transition-colors"
        >
          <Check className="w-4 h-4" />
          <span>¡Me la sé!</span>
        </button>

        <button
          onClick={handleNext}
          type="button"
          className="p-3 rounded-2xl bg-slate-900 border border-slate-800 hover:bg-slate-800 text-slate-300 cursor-pointer"
          title="Siguiente"
        >
          <ChevronRight className="w-5 h-5" />
        </button>
      </div>
    </div>
  );
};

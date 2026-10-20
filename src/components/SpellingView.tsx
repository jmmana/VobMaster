import React, { useState, useEffect } from 'react';
import confetti from 'canvas-confetti';
import { WordItem, GameSettings, UserProgress } from '../types';
import { WordIllustration } from './WordIllustration';
import { AudioPlayerButton } from './AudioPlayerButton';
import { audioService } from '../services/audioService';
import { 
  CheckCircle2, 
  XCircle, 
  ArrowRight, 
  Delete, 
  HelpCircle, 
  RotateCcw,
  Sparkles
} from 'lucide-react';

interface SpellingViewProps {
  words: WordItem[];
  settings: GameSettings;
  progress: UserProgress;
  onUpdateProgress: (updater: (prev: UserProgress) => UserProgress) => void;
}

export const SpellingView: React.FC<SpellingViewProps> = ({
  words,
  settings,
  progress,
  onUpdateProgress
}) => {
  const [currentWord, setCurrentWord] = useState<WordItem | null>(null);
  const [scrambledLetters, setScrambledLetters] = useState<{ id: string; char: string }[]>([]);
  const [userLetters, setUserLetters] = useState<{ id: string; char: string }[]>([]);
  const [isAnswered, setIsAnswered] = useState(false);
  const [isCorrect, setIsCorrect] = useState(false);
  const [hintUsed, setHintUsed] = useState(false);

  // Initialize new spelling round
  const pickNewWord = () => {
    // Pick words without spaces or special symbols for optimal spelling practice
    const candidatePool = words.filter(
      (w) => !w.word.includes(' ') && !w.word.includes('-') && w.word.length >= 3 && w.word.length <= 10
    );
    const target = candidatePool[Math.floor(Math.random() * candidatePool.length)];
    setCurrentWord(target);
    setUserLetters([]);
    setIsAnswered(false);
    setIsCorrect(false);
    setHintUsed(false);

    // Prepare scrambled tiles with unique ids
    const chars = target.word.toUpperCase().split('');
    const tiles = chars.map((char, index) => ({ id: `${char}-${index}-${Math.random()}`, char }));
    // Shuffle
    setScrambledLetters(tiles.sort(() => 0.5 - Math.random()));

    // Pronounce word
    audioService.speak(target.word, {
      rate: settings.speechRate,
      accent: settings.voiceAccent
    });
  };

  useEffect(() => {
    pickNewWord();
  }, [words]);

  const handleTileClick = (tile: { id: string; char: string }) => {
    if (isAnswered) return;
    audioService.playClickSound();

    setUserLetters([...userLetters, tile]);
    setScrambledLetters(scrambledLetters.filter((t) => t.id !== tile.id));
  };

  const handleRemoveLetter = (index: number) => {
    if (isAnswered) return;
    audioService.playClickSound();

    const removed = userLetters[index];
    const newUserLetters = [...userLetters];
    newUserLetters.splice(index, 1);
    setUserLetters(newUserLetters);
    setScrambledLetters([...scrambledLetters, removed]);
  };

  const handleCheck = () => {
    if (!currentWord) return;
    const constructed = userLetters.map((t) => t.char).join('');
    const target = currentWord.word.toUpperCase();

    setIsAnswered(true);
    if (constructed === target) {
      setIsCorrect(true);
      if (settings.soundEffects) {
        audioService.playCorrectSound();
      }
      confetti({ particleCount: 40, spread: 60 });
      onUpdateProgress((prev) => ({
        ...prev,
        score: prev.score + 150,
        streak: prev.streak + 1,
        bestStreak: Math.max(prev.bestStreak, prev.streak + 1),
        totalAnswered: prev.totalAnswered + 1,
        correctAnswers: prev.correctAnswers + 1
      }));
    } else {
      setIsCorrect(false);
      if (settings.soundEffects) {
        audioService.playWrongSound();
      }
      onUpdateProgress((prev) => ({
        ...prev,
        streak: 0,
        totalAnswered: prev.totalAnswered + 1
      }));
    }
  };

  const handleUseHint = () => {
    if (!currentWord || hintUsed || isAnswered) return;
    setHintUsed(true);
    // Find first missing letter
    const target = currentWord.word.toUpperCase().split('');
    const targetLetter = target[userLetters.length];
    const matchingTile = scrambledLetters.find((t) => t.char === targetLetter);
    if (matchingTile) {
      handleTileClick(matchingTile);
    }
  };

  if (!currentWord) return null;

  return (
    <div className="max-w-xl mx-auto px-4 py-8 flex flex-col items-center gap-6">
      {/* Top Title */}
      <div className="text-center">
        <h2 className="text-2xl font-bold text-white flex items-center justify-center gap-2">
          <span>Modo Deletreo & Constructor</span>
        </h2>
        <p className="text-xs text-slate-400 mt-1">
          Escucha la palabra, mira la imagen y ordena las fichas de letras:
        </p>
      </div>

      {/* Visual illustration and Audio Button */}
      <div className="w-full max-w-sm flex flex-col items-center gap-3">
        <WordIllustration word={currentWord} size="md" showDetails={isAnswered} />

        <div className="flex items-center gap-2">
          <AudioPlayerButton
            text={currentWord.word}
            size="lg"
            accent={settings.voiceAccent}
            rate={settings.speechRate}
            label="Escuchar palabra"
            autoPlay={true}
          />
        </div>

        <div className="bg-slate-900/80 px-4 py-2 rounded-xl border border-slate-800 text-center">
          <span className="text-xs text-slate-400 block font-medium">Traducción:</span>
          <span className="text-base font-bold text-emerald-300 capitalize">
            {currentWord.translation}
          </span>
        </div>
      </div>

      {/* Target letter slots / constructed word */}
      <div className="flex flex-wrap items-center justify-center gap-2 min-h-[64px] p-3 rounded-2xl bg-slate-900 border border-slate-800 w-full max-w-md">
        {userLetters.length === 0 ? (
          <span className="text-xs text-slate-500 italic">Haz clic en las letras abajo para formar la palabra</span>
        ) : (
          userLetters.map((tile, idx) => (
            <button
              key={tile.id}
              onClick={() => handleRemoveLetter(idx)}
              disabled={isAnswered}
              type="button"
              className="w-11 h-12 rounded-xl bg-emerald-600/90 text-white font-extrabold text-xl shadow-md flex items-center justify-center cursor-pointer hover:bg-rose-500 transition-colors"
            >
              {tile.char}
            </button>
          ))
        )}
      </div>

      {/* Available letter tiles pool */}
      <div className="flex flex-wrap items-center justify-center gap-2.5 max-w-md">
        {scrambledLetters.map((tile) => (
          <button
            key={tile.id}
            onClick={() => handleTileClick(tile)}
            disabled={isAnswered}
            type="button"
            className="w-12 h-13 rounded-2xl bg-slate-800 hover:bg-slate-700 active:scale-95 text-white font-extrabold text-xl shadow-lg border border-slate-700 flex items-center justify-center cursor-pointer transition-all"
          >
            {tile.char}
          </button>
        ))}
      </div>

      {/* Controls: Check, Hint, Next */}
      <div className="w-full max-w-md flex items-center justify-between gap-3 mt-2">
        {!isAnswered ? (
          <>
            <button
              onClick={handleUseHint}
              disabled={hintUsed || scrambledLetters.length === 0}
              type="button"
              className="px-4 py-3 rounded-xl bg-slate-800 text-slate-300 hover:text-white border border-slate-700 disabled:opacity-30 cursor-pointer flex items-center gap-1.5 text-xs font-semibold"
            >
              <HelpCircle className="w-4 h-4 text-amber-400" />
              <span>{hintUsed ? 'Pista usada' : 'Pista'}</span>
            </button>

            <button
              onClick={handleCheck}
              disabled={userLetters.length === 0}
              type="button"
              className="flex-1 py-3 px-6 rounded-xl bg-emerald-600 hover:bg-emerald-500 disabled:opacity-40 text-white font-bold text-sm shadow-md cursor-pointer transition-all"
            >
              Comprobar deletreo
            </button>
          </>
        ) : (
          <div className="w-full flex flex-col gap-3">
            <div
              className={`p-4 rounded-xl flex items-center justify-between ${
                isCorrect ? 'bg-emerald-950/40 border border-emerald-500/40 text-emerald-200' : 'bg-rose-950/40 border border-rose-500/40 text-rose-200'
              }`}
            >
              <div className="flex items-center gap-2">
                {isCorrect ? <CheckCircle2 className="w-5 h-5 text-emerald-400" /> : <XCircle className="w-5 h-5 text-rose-400" />}
                <span className="font-bold">
                  {isCorrect ? '¡Deletreo correcto!' : `Incorrecto. Era: ${currentWord.word.toUpperCase()}`}
                </span>
              </div>
            </div>

            <button
              onClick={pickNewWord}
              type="button"
              className="w-full py-3 px-6 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 text-white font-bold flex items-center justify-center gap-2 cursor-pointer shadow-lg"
            >
              <span>Siguiente palabra</span>
              <ArrowRight className="w-5 h-5" />
            </button>
          </div>
        )}
      </div>
    </div>
  );
};

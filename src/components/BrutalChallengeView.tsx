import React, { useState, useEffect, useMemo } from 'react';
import confetti from 'canvas-confetti';
import { 
  Flame, 
  Heart, 
  RotateCcw, 
  Volume2, 
  HelpCircle, 
  CheckCircle2, 
  XCircle, 
  ArrowRight, 
  Sparkles, 
  AlertTriangle, 
  Zap, 
  ShieldAlert,
  Trophy,
  Ear,
  FileQuestion,
  BookOpen
} from 'lucide-react';
import { brutalQuestions, BrutalQuestion, BrutalCategory } from '../data/brutalData';
import { audioService } from '../services/audioService';
import { GameSettings, UserProgress } from '../types';

interface BrutalChallengeViewProps {
  settings: GameSettings;
  progress: UserProgress;
  onUpdateProgress: (updater: (prev: UserProgress) => UserProgress) => void;
  onExit?: () => void;
}

export const BrutalChallengeView: React.FC<BrutalChallengeViewProps> = ({
  settings,
  progress,
  onUpdateProgress,
  onExit
}) => {
  const [selectedCategory, setSelectedCategory] = useState<BrutalCategory>('all');
  const [currentIndex, setCurrentIndex] = useState(0);
  const [selectedOption, setSelectedOption] = useState<string | null>(null);
  const [isAnswered, setIsAnswered] = useState(false);
  const [isCorrect, setIsCorrect] = useState(false);
  const [lives, setLives] = useState(3);
  const [roundScore, setRoundScore] = useState(0);
  const [roundStreak, setRoundStreak] = useState(0);
  const [trapsOvercome, setTrapsOvercome] = useState(0);
  const [isGameOver, setIsGameOver] = useState(false);
  const [isVictory, setIsVictory] = useState(false);
  const [shuffledOptions, setShuffledOptions] = useState<string[]>([]);

  // Filter pool by category
  const filteredQuestions = useMemo(() => {
    let pool = brutalQuestions;
    if (selectedCategory !== 'all') {
      pool = pool.filter((q) => q.category === selectedCategory);
    }
    // Shuffle pool for varied gameplay
    return [...pool].sort(() => Math.random() - 0.5);
  }, [selectedCategory]);

  const currentQ: BrutalQuestion | undefined = filteredQuestions[currentIndex];

  // Prepare question options
  useEffect(() => {
    if (currentQ) {
      const opts = [...currentQ.options].sort(() => Math.random() - 0.5);
      setShuffledOptions(opts);
      setSelectedOption(null);
      setIsAnswered(false);
      setIsCorrect(false);

      if (settings.autoPlayAudio) {
        audioService.speak(currentQ.audioText, {
          accent: settings.voiceAccent,
          rate: settings.speechRate
        });
      }
    }
  }, [currentIndex, currentQ, settings.autoPlayAudio, settings.voiceAccent, settings.speechRate]);

  // Restart challenge
  const handleRestart = () => {
    setCurrentIndex(0);
    setLives(3);
    setRoundScore(0);
    setRoundStreak(0);
    setTrapsOvercome(0);
    setIsGameOver(false);
    setIsVictory(false);
    setSelectedOption(null);
    setIsAnswered(false);
  };

  const handleSelectOption = (opt: string) => {
    if (isAnswered || !currentQ) return;

    setSelectedOption(opt);
    setIsAnswered(true);

    const correct = opt === currentQ.correctAnswer;
    setIsCorrect(correct);

    if (correct) {
      audioService.playCorrectSound();
      setRoundScore((prev) => prev + 100 + roundStreak * 15);
      setRoundStreak((prev) => prev + 1);
      setTrapsOvercome((prev) => prev + 1);

      // Trigger confetti on 3, 5, 10 streak
      if ((roundStreak + 1) % 3 === 0) {
        confetti({
          particleCount: 40,
          spread: 60,
          origin: { y: 0.7 }
        });
      }

      onUpdateProgress((prev) => ({
        ...prev,
        score: prev.score + 100,
        streak: prev.streak + 1,
        bestStreak: Math.max(prev.bestStreak, prev.streak + 1),
        totalAnswered: prev.totalAnswered + 1,
        correctAnswers: prev.correctAnswers + 1
      }));
    } else {
      audioService.playWrongSound();
      setRoundStreak(0);
      const nextLives = lives - 1;
      setLives(nextLives);

      onUpdateProgress((prev) => ({
        ...prev,
        streak: 0,
        totalAnswered: prev.totalAnswered + 1
      }));

      if (nextLives <= 0) {
        setIsGameOver(true);
      }
    }
  };

  const handleNext = () => {
    audioService.playClickSound();
    if (currentIndex + 1 >= filteredQuestions.length) {
      setIsVictory(true);
      confetti({
        particleCount: 100,
        spread: 80,
        origin: { y: 0.6 }
      });
    } else {
      setCurrentIndex((prev) => prev + 1);
    }
  };

  const playTargetAudio = (text: string, rateMultiplier: number = 1.0) => {
    audioService.speak(text, {
      accent: settings.voiceAccent,
      rate: settings.speechRate * rateMultiplier
    });
  };

  if (!currentQ && filteredQuestions.length === 0) {
    return (
      <div className="max-w-2xl mx-auto px-4 py-16 text-center">
        <p className="text-slate-400">No hay preguntas disponibles en esta categoría.</p>
        <button
          onClick={() => setSelectedCategory('all')}
          className="mt-4 px-4 py-2 bg-emerald-500 text-white rounded-xl font-bold cursor-pointer"
        >
          Ver Todas las Trampas
        </button>
      </div>
    );
  }

  return (
    <div className="max-w-4xl mx-auto px-4 py-6 flex flex-col gap-6">
      {/* Top Banner: Mode Identity */}
      <div className="relative overflow-hidden rounded-2xl bg-gradient-to-r from-rose-950/80 via-amber-950/70 to-slate-900 border border-rose-500/30 p-5 shadow-xl">
        <div className="relative z-10 flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div>
            <div className="flex items-center gap-2 mb-1">
              <span className="px-2.5 py-0.5 rounded-full bg-rose-500/20 text-rose-300 border border-rose-500/30 text-xs font-black uppercase tracking-wider flex items-center gap-1">
                <Flame className="w-3.5 h-3.5 text-rose-400 animate-pulse" />
                Reto Brutal &bull; Nivel Extremo
              </span>
              <span className="text-xs text-amber-300/80 font-semibold">
                Trampas del Inglés
              </span>
            </div>
            <h1 className="text-xl sm:text-2xl font-black text-white tracking-tight flex items-center gap-2">
              <span>Palabras que engañan a cualquiera</span>
              <span className="text-base sm:text-lg">💀</span>
            </h1>
            <p className="text-xs sm:text-sm text-slate-300 max-w-xl mt-1">
              Homófonos (suenan igual), homógrafos (se escriben igual) y falsos amigos (parecen español pero significan otra cosa).
            </p>
          </div>

          {/* Stats pills */}
          <div className="flex items-center gap-2 sm:gap-3 shrink-0">
            {/* Lives */}
            <div className="flex items-center gap-1 px-3 py-1.5 rounded-xl bg-slate-900/90 border border-rose-500/30 text-rose-400 font-bold text-sm">
              <Heart className={`w-4 h-4 fill-rose-500 text-rose-500 ${lives === 1 ? 'animate-bounce' : ''}`} />
              <span>{lives}</span>
            </div>

            {/* Streak */}
            <div className="flex items-center gap-1 px-3 py-1.5 rounded-xl bg-slate-900/90 border border-amber-500/30 text-amber-400 font-bold text-sm">
              <Flame className="w-4 h-4 text-amber-500" />
              <span>{roundStreak}</span>
            </div>

            {/* Score */}
            <div className="flex items-center gap-1 px-3 py-1.5 rounded-xl bg-slate-900/90 border border-emerald-500/30 text-emerald-400 font-bold text-sm">
              <Trophy className="w-4 h-4 text-emerald-400" />
              <span>{roundScore} pts</span>
            </div>
          </div>
        </div>

        {/* Decorative background glow */}
        <div className="absolute -top-12 -right-12 w-48 h-48 bg-rose-500/10 rounded-full blur-3xl pointer-events-none" />
      </div>

      {/* Sub-Category Filter Buttons */}
      <div className="flex items-center gap-1.5 overflow-x-auto pb-1 scrollbar-none">
        <button
          onClick={() => {
            setSelectedCategory('all');
            handleRestart();
          }}
          className={`px-3 py-1.5 rounded-xl text-xs font-bold whitespace-nowrap transition-all cursor-pointer ${
            selectedCategory === 'all'
              ? 'bg-rose-500 text-white shadow-md shadow-rose-950/50'
              : 'bg-slate-900 text-slate-400 hover:text-white border border-slate-800'
          }`}
        >
          🌟 Todas las Trampas ({brutalQuestions.length})
        </button>

        <button
          onClick={() => {
            setSelectedCategory('homophone');
            handleRestart();
          }}
          className={`px-3 py-1.5 rounded-xl text-xs font-bold whitespace-nowrap transition-all cursor-pointer flex items-center gap-1.5 ${
            selectedCategory === 'homophone'
              ? 'bg-rose-500 text-white shadow-md shadow-rose-950/50'
              : 'bg-slate-900 text-slate-400 hover:text-white border border-slate-800'
          }`}
        >
          <Ear className="w-3.5 h-3.5" />
          <span>Suenan Igual / Parecido (Desert, Bear...)</span>
        </button>

        <button
          onClick={() => {
            setSelectedCategory('false_friend');
            handleRestart();
          }}
          className={`px-3 py-1.5 rounded-xl text-xs font-bold whitespace-nowrap transition-all cursor-pointer flex items-center gap-1.5 ${
            selectedCategory === 'false_friend'
              ? 'bg-rose-500 text-white shadow-md shadow-rose-950/50'
              : 'bg-slate-900 text-slate-400 hover:text-white border border-slate-800'
          }`}
        >
          <AlertTriangle className="w-3.5 h-3.5" />
          <span>Falsos Amigos (Library ≠ Librería...)</span>
        </button>

        <button
          onClick={() => {
            setSelectedCategory('homograph');
            handleRestart();
          }}
          className={`px-3 py-1.5 rounded-xl text-xs font-bold whitespace-nowrap transition-all cursor-pointer flex items-center gap-1.5 ${
            selectedCategory === 'homograph'
              ? 'bg-rose-500 text-white shadow-md shadow-rose-950/50'
              : 'bg-slate-900 text-slate-400 hover:text-white border border-slate-800'
          }`}
        >
          <FileQuestion className="w-3.5 h-3.5" />
          <span>Se escriben igual (Tear, Lead...)</span>
        </button>
      </div>

      {/* Progress Bar */}
      <div className="w-full bg-slate-900 rounded-full h-2 overflow-hidden border border-slate-800">
        <div 
          className="bg-gradient-to-r from-rose-500 to-amber-400 h-full transition-all duration-300"
          style={{ width: `${((currentIndex + 1) / filteredQuestions.length) * 100}%` }}
        />
      </div>

      {/* Main Challenge Card */}
      {currentQ && !isGameOver && !isVictory && (
        <div className="bg-slate-900/90 border border-slate-800 rounded-3xl p-6 sm:p-8 flex flex-col gap-6 shadow-2xl relative">
          {/* Card Header: Type Badge & Question Counter */}
          <div className="flex items-center justify-between text-xs">
            <span className="px-3 py-1 rounded-full bg-amber-500/20 text-amber-300 border border-amber-500/30 font-bold">
              {currentQ.typeLabel}
            </span>
            <span className="text-slate-400 font-bold">
              Pregunta {currentIndex + 1} de {filteredQuestions.length}
            </span>
          </div>

          {/* Central Question Display */}
          <div className="flex flex-col items-center text-center gap-3 py-2">
            <h2 className="text-lg sm:text-2xl font-bold text-white max-w-xl">
              {currentQ.prompt}
            </h2>

            {/* Target Word Display with IPA and Audio */}
            <div className="flex flex-wrap items-center justify-center gap-3 mt-1">
              <div className="px-5 py-2.5 rounded-2xl bg-slate-950 border border-slate-800 flex items-center gap-3 shadow-inner">
                <span className="text-2xl sm:text-3xl font-black text-rose-400 uppercase tracking-wide">
                  {currentQ.targetWord}
                </span>
                <span className="text-xs sm:text-sm font-mono text-slate-400">
                  {currentQ.phonetic}
                </span>
              </div>

              {/* Audio Listen Buttons */}
              <div className="flex items-center gap-2">
                <button
                  type="button"
                  onClick={() => playTargetAudio(currentQ.targetWord, 1.0)}
                  className="p-3 rounded-2xl bg-rose-500 hover:bg-rose-400 text-white font-bold transition-all shadow-lg shadow-rose-950/40 cursor-pointer flex items-center gap-1.5"
                  title="Escuchar pronunciación nativa"
                >
                  <Volume2 className="w-5 h-5" />
                  <span className="text-xs hidden sm:inline">Audio</span>
                </button>

                <button
                  type="button"
                  onClick={() => playTargetAudio(currentQ.targetWord, 0.7)}
                  className="p-3 rounded-2xl bg-slate-800 hover:bg-slate-700 text-amber-300 font-bold transition-all border border-slate-700 cursor-pointer flex items-center gap-1 text-xs"
                  title="Escuchar en velocidad lenta"
                >
                  <span>🐢</span>
                  <span className="hidden sm:inline">Lento</span>
                </button>
              </div>
            </div>

            {/* Context Sentence in English */}
            {currentQ.contextSentence && (
              <div className="bg-slate-950/60 border border-slate-800/80 rounded-2xl px-4 py-2.5 max-w-lg mt-2 text-slate-300 text-xs sm:text-sm italic">
                "{currentQ.contextSentence}"
              </div>
            )}
          </div>

          {/* 4 Options Grid */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-2">
            {shuffledOptions.map((opt, idx) => {
              const isSelected = selectedOption === opt;
              const isTargetCorrect = opt === currentQ.correctAnswer;

              let btnStyle = 'bg-slate-950/80 hover:bg-slate-800/90 text-slate-200 border-slate-800 hover:border-slate-700';

              if (isAnswered) {
                if (isTargetCorrect) {
                  btnStyle = 'bg-emerald-950/80 text-emerald-200 border-emerald-500 ring-2 ring-emerald-500/50 font-black';
                } else if (isSelected) {
                  btnStyle = 'bg-rose-950/80 text-rose-200 border-rose-500 ring-2 ring-rose-500/50 line-through opacity-80';
                } else {
                  btnStyle = 'bg-slate-950/40 text-slate-500 border-slate-900 opacity-40';
                }
              }

              return (
                <button
                  key={idx}
                  type="button"
                  disabled={isAnswered}
                  onClick={() => handleSelectOption(opt)}
                  className={`p-4 rounded-2xl border text-left text-sm sm:text-base font-bold transition-all flex items-center justify-between gap-3 cursor-pointer ${btnStyle}`}
                >
                  <span>{opt}</span>
                  {isAnswered && isTargetCorrect && (
                    <CheckCircle2 className="w-5 h-5 text-emerald-400 shrink-0" />
                  )}
                  {isAnswered && isSelected && !isTargetCorrect && (
                    <XCircle className="w-5 h-5 text-rose-400 shrink-0" />
                  )}
                </button>
              );
            })}
          </div>

          {/* Trap Breakdown & Explanation Card (Shown immediately upon answer) */}
          {isAnswered && (
            <div className={`rounded-2xl p-5 border flex flex-col gap-4 animate-in fade-in slide-in-from-bottom-3 duration-300 ${
              isCorrect 
                ? 'bg-emerald-950/40 border-emerald-500/40' 
                : 'bg-rose-950/40 border-rose-500/40'
            }`}>
              {/* Header result */}
              <div className="flex items-center justify-between gap-3">
                <div className="flex items-center gap-2">
                  {isCorrect ? (
                    <div className="w-8 h-8 rounded-xl bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-bold">
                      ✓
                    </div>
                  ) : (
                    <div className="w-8 h-8 rounded-xl bg-rose-500/20 text-rose-400 flex items-center justify-center font-bold">
                      ✗
                    </div>
                  )}
                  <div>
                    <h3 className="font-bold text-white text-sm sm:text-base">
                      {isCorrect ? '¡Excelente! Esquivaste la trampa' : '¡Caíste en la trampa habitual!'}
                    </h3>
                    <p className="text-xs text-slate-300 font-medium">
                      {currentQ.explanation.title}
                    </p>
                  </div>
                </div>

                {/* Next button */}
                <button
                  onClick={handleNext}
                  type="button"
                  className="px-5 py-2.5 rounded-xl bg-emerald-500 hover:bg-emerald-400 text-white font-black text-sm flex items-center gap-2 shadow-lg shadow-emerald-950/50 cursor-pointer transition-all"
                >
                  <span>Siguiente</span>
                  <ArrowRight className="w-4 h-4" />
                </button>
              </div>

              {/* Educational Explanation */}
              <p className="text-xs sm:text-sm text-slate-200 leading-relaxed whitespace-pre-line bg-slate-950/60 p-3 rounded-xl border border-slate-800">
                {currentQ.explanation.description}
              </p>

              {/* Memory Trick */}
              {currentQ.explanation.trick && (
                <div className="text-xs sm:text-sm text-amber-200 font-semibold bg-amber-500/10 border border-amber-500/20 px-3.5 py-2 rounded-xl">
                  {currentQ.explanation.trick}
                </div>
              )}

              {/* Side-by-side Audio Comparison for Confusable Words */}
              {currentQ.confusables && currentQ.confusables.length > 0 && (
                <div className="flex flex-col gap-2 pt-1 border-t border-slate-800/80">
                  <span className="text-[11px] font-bold text-slate-400 uppercase tracking-wider">
                    🔊 Escucha y Compara la diferencia:
                  </span>
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                    {currentQ.confusables.map((item, cIdx) => (
                      <div
                        key={cIdx}
                        className="bg-slate-950/80 border border-slate-800 rounded-xl p-3 flex items-center justify-between gap-2"
                      >
                        <div className="flex items-center gap-2.5">
                          <span className="text-xl">{item.emoji}</span>
                          <div>
                            <div className="flex items-center gap-1.5">
                              <span className="font-black text-sm text-white">
                                {item.word}
                              </span>
                              <span className="text-[11px] font-mono text-slate-400">
                                {item.phonetic}
                              </span>
                            </div>
                            <span className="text-xs text-slate-300">
                              {item.meaning}
                            </span>
                          </div>
                        </div>

                        {/* Audio Button */}
                        <button
                          type="button"
                          onClick={() => playTargetAudio(item.word, 0.9)}
                          className="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-rose-300 hover:text-white transition-colors cursor-pointer"
                          title={`Escuchar ${item.word}`}
                        >
                          <Volume2 className="w-4 h-4" />
                        </button>
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>
          )}
        </div>
      )}

      {/* Game Over Screen */}
      {isGameOver && (
        <div className="bg-slate-900 border border-rose-500/40 rounded-3xl p-8 text-center flex flex-col items-center gap-5 shadow-2xl animate-in zoom-in-95 duration-300">
          <div className="w-20 h-20 rounded-full bg-rose-500/20 text-rose-400 flex items-center justify-center text-3xl border border-rose-500/30">
            💀
          </div>
          <div>
            <h2 className="text-2xl font-black text-white">¡Las trampas te atraparon!</h2>
            <p className="text-slate-400 text-sm mt-1 max-w-md">
              Estas palabras engañan incluso a estudiantes avanzados. ¡Vuelve a intentarlo para dominar los homófonos y falsos amigos!
            </p>
          </div>

          <div className="flex items-center gap-6 py-2">
            <div>
              <span className="text-xs text-slate-500 block">Puntaje</span>
              <span className="text-xl font-black text-white">{roundScore} pts</span>
            </div>
            <div className="w-px h-8 bg-slate-800" />
            <div>
              <span className="text-xs text-slate-500 block">Trampas Superadas</span>
              <span className="text-xl font-black text-emerald-400">{trapsOvercome}</span>
            </div>
          </div>

          <button
            type="button"
            onClick={handleRestart}
            className="px-6 py-3 rounded-2xl bg-rose-500 hover:bg-rose-400 text-white font-black text-sm flex items-center gap-2 shadow-lg shadow-rose-950/50 cursor-pointer transition-all"
          >
            <RotateCcw className="w-4 h-4" />
            <span>Reintentar Reto Brutal</span>
          </button>
        </div>
      )}

      {/* Victory Screen */}
      {isVictory && (
        <div className="bg-slate-900 border border-emerald-500/40 rounded-3xl p-8 text-center flex flex-col items-center gap-5 shadow-2xl animate-in zoom-in-95 duration-300">
          <div className="w-20 h-20 rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center text-3xl border border-emerald-500/30 animate-bounce">
            👑
          </div>
          <div>
            <h2 className="text-2xl font-black text-white">¡Sobreviviste al Reto Brutal!</h2>
            <p className="text-slate-300 text-sm mt-1 max-w-md">
              ¡Increíble maestría! Ya no te confundes con desert/dessert, bear/beard/beer, ni library/bookstore.
            </p>
          </div>

          <div className="flex items-center gap-6 py-2">
            <div>
              <span className="text-xs text-slate-500 block">Puntaje Final</span>
              <span className="text-2xl font-black text-amber-400">{roundScore} pts</span>
            </div>
            <div className="w-px h-8 bg-slate-800" />
            <div>
              <span className="text-xs text-slate-500 block">Trampas Vencidas</span>
              <span className="text-2xl font-black text-emerald-400">{trapsOvercome} / {filteredQuestions.length}</span>
            </div>
          </div>

          <div className="flex items-center gap-3">
            <button
              type="button"
              onClick={handleRestart}
              className="px-6 py-3 rounded-2xl bg-emerald-500 hover:bg-emerald-400 text-white font-black text-sm flex items-center gap-2 shadow-lg shadow-emerald-950/50 cursor-pointer transition-all"
            >
              <RotateCcw className="w-4 h-4" />
              <span>Jugar Otra Ronda</span>
            </button>

            {onExit && (
              <button
                type="button"
                onClick={onExit}
                className="px-5 py-3 rounded-2xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-sm cursor-pointer transition-all"
              >
                Volver
              </button>
            )}
          </div>
        </div>
      )}
    </div>
  );
};

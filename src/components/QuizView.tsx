import React, { useState, useEffect, useMemo } from 'react';
import confetti from 'canvas-confetti';
import { WordItem, QuizQuestion, GameSettings, UserProgress } from '../types';
import { WordIllustration } from './WordIllustration';
import { AudioPlayerButton } from './AudioPlayerButton';
import { audioService } from '../services/audioService';
import { 
  Volume2, 
  HelpCircle, 
  CheckCircle2, 
  XCircle, 
  ArrowRight, 
  RotateCcw, 
  Flame, 
  Trophy, 
  Eye, 
  EyeOff, 
  Sparkles,
  Heart,
  VolumeX,
  Shuffle,
  Clock,
  Zap
} from 'lucide-react';

interface QuizViewProps {
  words: WordItem[];
  settings: GameSettings;
  progress: UserProgress;
  onUpdateProgress: (updater: (prev: UserProgress) => UserProgress) => void;
  mode: 'listen' | 'visual' | 'mixed';
  onExit?: () => void;
}

export const QuizView: React.FC<QuizViewProps> = ({
  words,
  settings,
  progress,
  onUpdateProgress,
  mode,
  onExit
}) => {
  // Filter available word pool based on user settings
  const filteredWords = useMemo(() => {
    let pool = words;
    if (settings.selectedCategory !== 'all') {
      pool = pool.filter((w) => w.categoryId === settings.selectedCategory);
    }
    if (settings.selectedLevel !== 'all') {
      pool = pool.filter((w) => w.level === settings.selectedLevel);
    }
    return pool.length >= 4 ? pool : words;
  }, [words, settings.selectedCategory, settings.selectedLevel]);

  // Current Question State
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [currentQuestion, setCurrentQuestion] = useState<QuizQuestion | null>(null);
  const [selectedAnswer, setSelectedAnswer] = useState<string | null>(null);
  const [isAnswered, setIsAnswered] = useState(false);
  const [isCorrect, setIsCorrect] = useState(false);
  const [lives, setLives] = useState(3);
  const [roundScore, setRoundScore] = useState(0);
  const [roundStreak, setRoundStreak] = useState(0);
  const [showImageInAudioMode, setShowImageInAudioMode] = useState(false);
  const isExpertMode = settings.quizDifficulty === 'expert';
  const initialTime = settings.timerSeconds || 15;
  const [timeLeft, setTimeLeft] = useState(initialTime);

  // Generate a new question
  const generateQuestion = (index: number): QuizQuestion => {
    // Pick random target word from filtered pool
    const target = filteredWords[Math.floor(Math.random() * filteredWords.length)];

    // Determine prompt type
    let promptType: QuizQuestion['type'] = 'visual_choose_en';
    let promptMode: 'audio' | 'visual' | 'both' = 'visual';

    if (mode === 'listen') {
      promptType = Math.random() > 0.5 ? 'listen_choose_es' : 'listen_choose_en';
      promptMode = 'audio';
    } else if (mode === 'visual') {
      promptType = Math.random() > 0.5 ? 'visual_choose_en' : 'visual_choose_es';
      promptMode = 'visual';
    } else {
      // Mixed mode
      const rand = Math.random();
      if (rand < 0.4) {
        promptType = 'listen_choose_es';
        promptMode = 'audio';
      } else if (rand < 0.8) {
        promptType = 'visual_choose_en';
        promptMode = 'visual';
      } else {
        promptType = 'listen_choose_en';
        promptMode = 'both';
      }
    }

    // Determine correct answer and distractor options
    const isEnAnswer = promptType === 'listen_choose_en' || promptType === 'visual_choose_en';
    const correctAnswer = isEnAnswer ? target.word : target.translation;

    // Pick 3 distractors for Normal (4 total), or 5 distractors for Hard/Expert (6 total)
    const numDistractors = (settings.quizDifficulty === 'hard' || settings.quizDifficulty === 'expert') ? 5 : 3;
    const categoryPool = filteredWords.filter((w) => w.id !== target.id);
    const shuffledPool = [...categoryPool].sort(() => 0.5 - Math.random());
    const distractors = shuffledPool
      .slice(0, numDistractors)
      .map((w) => (isEnAnswer ? w.word : w.translation));

    // Combine and shuffle options
    const options = [correctAnswer, ...distractors].sort(() => 0.5 - Math.random());

    return {
      targetWord: target,
      type: promptType,
      options,
      correctAnswer,
      promptMode
    };
  };

  // Start round / Next Question
  useEffect(() => {
    setShowImageInAudioMode(false);
    setSelectedAnswer(null);
    setIsAnswered(false);
    setTimeLeft(initialTime);
    setCurrentQuestion(generateQuestion(currentQuestionIndex));
  }, [currentQuestionIndex, mode, settings.selectedCategory, settings.selectedLevel, settings.quizDifficulty]);

  // Countdown timer for Expert Mode
  useEffect(() => {
    if (!isExpertMode || isAnswered || !currentQuestion) return;

    if (timeLeft <= 0) {
      handleTimeout();
      return;
    }

    const interval = setInterval(() => {
      setTimeLeft((prev) => {
        if (prev <= 1) {
          clearInterval(interval);
          handleTimeout();
          return 0;
        }
        return prev - 1;
      });
    }, 1000);

    return () => clearInterval(interval);
  }, [timeLeft, isExpertMode, isAnswered, currentQuestion]);

  const handleTimeout = () => {
    if (isAnswered || !currentQuestion) return;
    setIsAnswered(true);
    setIsCorrect(false);
    setSelectedAnswer('__TIMEOUT__');

    if (settings.soundEffects) {
      audioService.playWrongSound();
    }
    setRoundStreak(0);
    setLives((prev) => Math.max(0, prev - 1));

    onUpdateProgress((prev) => ({
      ...prev,
      streak: 0,
      totalAnswered: prev.totalAnswered + 1,
      mistakeWordIds: prev.mistakeWordIds.includes(currentQuestion.targetWord.id)
        ? prev.mistakeWordIds
        : [...prev.mistakeWordIds, currentQuestion.targetWord.id]
    }));
  };

  // Handle Answer Selection
  const handleSelectOption = (option: string) => {
    if (isAnswered || !currentQuestion) return;

    setSelectedAnswer(option);
    setIsAnswered(true);

    const correct = option.trim().toLowerCase() === currentQuestion.correctAnswer.trim().toLowerCase();
    setIsCorrect(correct);

    if (correct) {
      if (settings.soundEffects) {
        audioService.playCorrectSound();
      }

      const newStreak = roundStreak + 1;
      setRoundStreak(newStreak);
      const points = 100 + newStreak * 20;
      setRoundScore((prev) => prev + points);

      if (newStreak >= 3 && settings.soundEffects) {
        audioService.playStreakSound();
      }

      // Trigger Confetti on streak or high score
      if (newStreak % 3 === 0) {
        confetti({
          particleCount: 50,
          spread: 60,
          origin: { y: 0.7 }
        });
      }

      // Update global user progress
      onUpdateProgress((prev) => {
        const mastered = prev.masteredWordIds.includes(currentQuestion.targetWord.id)
          ? prev.masteredWordIds
          : [...prev.masteredWordIds, currentQuestion.targetWord.id];

        const mistakeList = prev.mistakeWordIds.filter((id) => id !== currentQuestion.targetWord.id);
        const best = Math.max(prev.bestStreak, newStreak);

        return {
          ...prev,
          score: prev.score + points,
          streak: newStreak,
          bestStreak: best,
          totalAnswered: prev.totalAnswered + 1,
          correctAnswers: prev.correctAnswers + 1,
          masteredWordIds: mastered,
          mistakeWordIds: mistakeList
        };
      });
    } else {
      if (settings.soundEffects) {
        audioService.playWrongSound();
      }

      setRoundStreak(0);
      setLives((prev) => Math.max(0, prev - 1));

      // Record mistake
      onUpdateProgress((prev) => {
        const mistakeList = prev.mistakeWordIds.includes(currentQuestion.targetWord.id)
          ? prev.mistakeWordIds
          : [...prev.mistakeWordIds, currentQuestion.targetWord.id];

        return {
          ...prev,
          streak: 0,
          totalAnswered: prev.totalAnswered + 1,
          mistakeWordIds: mistakeList
        };
      });
    }

    // Always pronounce the word on answer selection so the user hears correct audio!
    audioService.speak(currentQuestion.targetWord.word, {
      rate: settings.speechRate,
      accent: settings.voiceAccent
    });
  };

  // Next Question
  const handleNext = () => {
    audioService.playClickSound();
    setCurrentQuestionIndex((prev) => prev + 1);
  };

  // Reset / Play Again
  const handleRestart = () => {
    audioService.playClickSound();
    setLives(3);
    setRoundScore(0);
    setRoundStreak(0);
    setCurrentQuestionIndex(0);
  };

  if (!currentQuestion) {
    return (
      <div className="flex items-center justify-center p-12 text-slate-400">
        Cargando vocabulario...
      </div>
    );
  }

  const { targetWord, promptMode, options, correctAnswer } = currentQuestion;

  return (
    <div className="max-w-2xl mx-auto px-4 py-4 sm:py-8 flex flex-col gap-6">
      {/* Top Game Bar: Lives, Streak, Points & Counter */}
      <div className="flex items-center justify-between bg-slate-900/80 backdrop-blur-md px-5 py-3 rounded-2xl border border-slate-800 shadow-xl">
        {/* Lives / Practice Indicator */}
        <div className="flex items-center gap-1.5">
          {[1, 2, 3].map((heart) => (
            <Heart
              key={heart}
              className={`w-5 h-5 transition-transform ${
                heart <= lives
                  ? 'fill-rose-500 text-rose-500 scale-100'
                  : 'fill-slate-800 text-slate-700 scale-90'
              }`}
            />
          ))}
        </div>

        {/* Combo Streak */}
        <div className="flex items-center gap-1.5 bg-amber-500/10 px-3 py-1 rounded-full border border-amber-500/30 text-amber-400 font-bold text-sm">
          <Flame className="w-4 h-4 text-amber-500 animate-pulse" />
          <span>{roundStreak} Racha</span>
        </div>

        {/* Points */}
        <div className="flex items-center gap-1.5 text-emerald-400 font-bold text-sm">
          <Trophy className="w-4 h-4 text-emerald-500" />
          <span>{roundScore} pts</span>
        </div>
      </div>

      {/* Main Challenge Card */}
      <div className="bg-slate-900/90 backdrop-blur-xl rounded-3xl p-6 sm:p-8 border border-slate-800/80 shadow-2xl relative flex flex-col items-center">
        
        {/* Instruction & Level Badges */}
        <div className="mb-3 flex items-center flex-wrap justify-center gap-2">
          {/* Level Badge */}
          <span className={`px-2.5 py-0.5 rounded-full text-xs font-bold border ${
            targetWord.level === 'A1' ? 'bg-emerald-500/20 text-emerald-300 border-emerald-500/30' :
            targetWord.level === 'A2' ? 'bg-sky-500/20 text-sky-300 border-sky-500/30' :
            targetWord.level === 'B1' ? 'bg-yellow-500/20 text-yellow-300 border-yellow-500/30' :
            targetWord.level === 'B2' ? 'bg-orange-500/20 text-orange-300 border-orange-500/30' :
            'bg-rose-500/20 text-rose-300 border-rose-500/30'
          }`}>
            Nivel {targetWord.level}
          </span>

          {/* Category */}
          <span className="px-2.5 py-0.5 rounded-full text-xs font-medium bg-slate-800 text-slate-300 border border-slate-700/60">
            {targetWord.category}
          </span>

          {/* Mode Badge */}
          <div className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-slate-800/90 text-xs font-medium text-slate-300 border border-slate-700/60">
            {promptMode === 'audio' ? (
              <>
                <Volume2 className="w-3.5 h-3.5 text-emerald-400" />
                <span>Audio</span>
              </>
            ) : promptMode === 'visual' ? (
              <>
                <Eye className="w-3.5 h-3.5 text-sky-400" />
                <span>Visual</span>
              </>
            ) : (
              <>
                <Sparkles className="w-3.5 h-3.5 text-amber-400" />
                <span>Mixto</span>
              </>
            )}
          </div>

          {/* Challenge mode badge */}
          {settings.quizDifficulty === 'hard' && (
            <span className="px-2.5 py-0.5 rounded-full text-xs font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30 flex items-center gap-1">
              <Zap className="w-3 h-3" /> 6 Opciones (Difícil)
            </span>
          )}
          {isExpertMode && (
            <span className={`px-2.5 py-0.5 rounded-full text-xs font-bold border flex items-center gap-1 ${
              timeLeft <= 5 
                ? 'bg-rose-500/30 text-rose-300 border-rose-500 animate-pulse'
                : 'bg-amber-500/20 text-amber-300 border-amber-500/30'
            }`}>
              <Clock className="w-3 h-3" /> {timeLeft}s
            </span>
          )}
        </div>

        {/* Expert Countdown Progress Bar */}
        {isExpertMode && !isAnswered && (
          <div className="w-full max-w-sm mb-3">
            <div className="w-full h-2 rounded-full bg-slate-800 overflow-hidden">
              <div 
                className={`h-full transition-all duration-1000 rounded-full ${
                  timeLeft <= 5 ? 'bg-rose-500' : timeLeft <= 10 ? 'bg-amber-500' : 'bg-emerald-500'
                }`}
                style={{ width: `${Math.max(0, (timeLeft / initialTime) * 100)}%` }}
              />
            </div>
          </div>
        )}

        {/* Central Display: Image Card or Big Audio Button */}
        <div className="w-full flex flex-col items-center gap-4 my-2">
          {promptMode === 'visual' || promptMode === 'both' || showImageInAudioMode || isAnswered ? (
            <div className="w-full max-w-sm transition-all duration-300">
              <WordIllustration word={targetWord} size="lg" showDetails={isAnswered} />
            </div>
          ) : (
            /* Audio First Mode: Big sound prompt card */
            <div className="w-full max-w-sm h-56 rounded-2xl bg-gradient-to-br from-slate-900 to-slate-800 border border-slate-700/60 flex flex-col items-center justify-center p-6 text-center gap-4 shadow-inner">
              <div className="w-20 h-20 rounded-full bg-emerald-500/20 border border-emerald-500/40 flex items-center justify-center">
                <Volume2 className="w-10 h-10 text-emerald-400 animate-pulse" />
              </div>
              <p className="text-slate-300 font-medium text-sm">
                Escucha atentamente la pronunciación en inglés
              </p>
              <button
                type="button"
                onClick={() => setShowImageInAudioMode(true)}
                className="text-xs text-slate-400 hover:text-slate-200 inline-flex items-center gap-1 underline underline-offset-4 cursor-pointer"
              >
                <Eye className="w-3.5 h-3.5" />
                <span>¿Ver pista visual?</span>
              </button>
            </div>
          )}

          {/* Interactive Audio Pronunciation Controller */}
          <div className="flex flex-col items-center gap-2 mt-2">
            <AudioPlayerButton
              text={targetWord.word}
              size={promptMode === 'audio' ? 'hero' : 'lg'}
              accent={settings.voiceAccent}
              rate={settings.speechRate}
              label={promptMode === 'audio' ? 'Escuchar palabra' : 'Pronunciación'}
              autoPlay={settings.autoPlayAudio}
            />
            {isAnswered && (
              <span className="text-slate-400 text-sm font-mono tracking-wider">
                {targetWord.phonetic}
              </span>
            )}
          </div>
        </div>

        {/* Question Title */}
        <h3 className="text-center font-bold text-lg sm:text-xl text-slate-100 mt-3 mb-1">
          {currentQuestion.type === 'visual_choose_en' || currentQuestion.type === 'listen_choose_en'
            ? '¿Cómo se dice en inglés?'
            : '¿Cuál es el significado correcto en español?'}
        </h3>
        <p className="text-xs text-slate-400 text-center mb-6">
          Selecciona una de las {options.length} opciones abajo:
        </p>

        {/* Interactive Answer Options (2 columns for 4 options, 3 columns on larger screens for 6 options) */}
        <div className={`grid gap-3.5 w-full ${options.length > 4 ? 'grid-cols-1 sm:grid-cols-2 md:grid-cols-3' : 'grid-cols-1 sm:grid-cols-2'}`}>
          {options.map((option, idx) => {
            const isSelected = selectedAnswer === option;
            const isOptionCorrect = option.trim().toLowerCase() === correctAnswer.trim().toLowerCase();

            let optionStyle = 'bg-slate-800/80 hover:bg-slate-700/80 text-slate-100 border-slate-700/70 hover:border-slate-500';

            if (isAnswered) {
              if (isOptionCorrect) {
                optionStyle = 'bg-emerald-500/20 text-emerald-200 border-emerald-500 ring-2 ring-emerald-500/40 font-bold';
              } else if (isSelected && !isOptionCorrect) {
                optionStyle = 'bg-rose-500/20 text-rose-200 border-rose-500 ring-2 ring-rose-500/40 line-through opacity-80';
              } else {
                optionStyle = 'bg-slate-900/40 text-slate-500 border-slate-800 opacity-50';
              }
            }

            return (
              <button
                key={idx}
                type="button"
                disabled={isAnswered}
                onClick={() => handleSelectOption(option)}
                className={`p-4 rounded-xl text-left border flex items-center justify-between transition-all duration-200 cursor-pointer active:scale-98 shadow-sm ${optionStyle}`}
              >
                <div className="flex items-center gap-3">
                  <span className="w-6 h-6 rounded-full bg-black/30 border border-white/10 flex items-center justify-center text-xs font-bold text-slate-300">
                    {String.fromCharCode(65 + idx)}
                  </span>
                  <span className="font-semibold text-base capitalize">{option}</span>
                </div>

                {/* Feedback Icons */}
                {isAnswered && (
                  <div>
                    {isOptionCorrect && <CheckCircle2 className="w-5 h-5 text-emerald-400" />}
                    {isSelected && !isOptionCorrect && <XCircle className="w-5 h-5 text-rose-400" />}
                  </div>
                )}
              </button>
            );
          })}
        </div>

        {/* Detailed Feedback & Learning Card (Shown immediately upon answering) */}
        {isAnswered && (
          <div className="w-full mt-6 pt-5 border-t border-slate-800 flex flex-col gap-4 animate-in fade-in duration-300">
            {/* Success / Error Banner */}
            <div
              className={`p-4 rounded-2xl flex items-start justify-between gap-3 ${
                isCorrect ? 'bg-emerald-950/40 border border-emerald-500/40 text-emerald-200' : 'bg-rose-950/40 border border-rose-500/40 text-rose-200'
              }`}
            >
              <div>
                <p className="font-bold text-base flex items-center gap-1.5">
                  {isCorrect ? (
                    <>
                      <CheckCircle2 className="w-5 h-5 text-emerald-400" />
                      <span>¡Excelente! Respuesta correcta</span>
                    </>
                  ) : (
                    <>
                      <XCircle className="w-5 h-5 text-rose-400" />
                      <span>¡Casi! La respuesta correcta era: <strong>{correctAnswer}</strong></span>
                    </>
                  )}
                </p>
                <p className="text-sm mt-1 text-slate-300">
                  <strong className="text-white capitalize">{targetWord.word}</strong>: {targetWord.translation}
                </p>
              </div>

              <AudioPlayerButton
                text={targetWord.word}
                size="sm"
                accent={settings.voiceAccent}
                rate={settings.speechRate}
              />
            </div>

            {/* Contextual Example Sentence with audio */}
            <div className="bg-slate-800/40 rounded-xl p-3.5 border border-slate-800 text-sm flex flex-col gap-1">
              <div className="flex items-center justify-between">
                <span className="text-xs uppercase tracking-wider font-bold text-emerald-400">Ejemplo en contexto:</span>
                <AudioPlayerButton
                  text={targetWord.example}
                  size="sm"
                  accent={settings.voiceAccent}
                  rate={0.9}
                />
              </div>
              <p className="text-slate-100 font-medium italic">"{targetWord.example}"</p>
              <p className="text-slate-400 text-xs">{targetWord.exampleEs}</p>
            </div>

            {/* Next Word Button */}
            <button
              onClick={handleNext}
              type="button"
              className="w-full py-4 px-6 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white font-bold text-base shadow-lg shadow-emerald-900/30 flex items-center justify-center gap-2 cursor-pointer transition-transform active:scale-98"
            >
              <span>Siguiente palabra</span>
              <ArrowRight className="w-5 h-5" />
            </button>
          </div>
        )}
      </div>

      {/* Game Over Modal / Lives empty */}
      {lives === 0 && (
        <div className="fixed inset-0 bg-black/80 backdrop-blur-md flex items-center justify-center p-4 z-50 animate-in fade-in">
          <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6 sm:p-8 max-w-md w-full text-center flex flex-col items-center gap-4 shadow-2xl">
            <div className="w-16 h-16 rounded-full bg-rose-500/20 text-rose-400 flex items-center justify-center border border-rose-500/30">
              <Heart className="w-8 h-8 fill-rose-500/40" />
            </div>
            <h3 className="text-2xl font-bold text-white">¡Ronda terminada!</h3>
            <p className="text-slate-300 text-sm">
              Has practicado con éxito. Obtuviste <strong>{roundScore} puntos</strong> en esta sesión.
            </p>
            <div className="w-full flex gap-3 mt-2">
              <button
                onClick={handleRestart}
                type="button"
                className="flex-1 py-3 px-4 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold flex items-center justify-center gap-2 cursor-pointer"
              >
                <RotateCcw className="w-4 h-4" />
                <span>Jugar de nuevo</span>
              </button>
              {onExit && (
                <button
                  onClick={onExit}
                  type="button"
                  className="py-3 px-4 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold cursor-pointer"
                >
                  Menú
                </button>
              )}
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

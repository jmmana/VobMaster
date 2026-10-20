export type CEFRLevel = 'A1' | 'A2' | 'B1' | 'B2' | 'C1';

export interface WordItem {
  id: number;
  word: string;
  translation: string;
  level: CEFRLevel;
  category: string;
  categoryId: string;
  phonetic: string;
  example: string;
  exampleEs: string;
  emoji: string;
  visualColor: string;
  imageKeywords?: string;
}

export interface CategoryItem {
  id: string;
  name: string;
  emoji: string;
  icon: string;
  color: string;
  count: number;
}

export type GameMode = 'listen' | 'visual' | 'mixed' | 'spelling' | 'flashcards' | 'speed';

export interface QuizQuestion {
  targetWord: WordItem;
  type: 'listen_choose_es' | 'listen_choose_en' | 'visual_choose_en' | 'visual_choose_es' | 'spelling';
  options: string[];
  correctAnswer: string;
  promptMode: 'audio' | 'visual' | 'both';
}

export type QuizChallengeLevel = 'normal' | 'hard' | 'expert';

export interface GameSettings {
  speechRate: number; // 0.7 to 1.2
  voiceAccent: 'US' | 'UK' | 'AU';
  autoPlayAudio: boolean;
  soundEffects: boolean;
  selectedCategory: string | 'all';
  selectedLevel: CEFRLevel | 'all';
  questionsPerRound: number;
  quizDifficulty: QuizChallengeLevel; // 'normal' (4 options), 'hard' (6 options), 'expert' (6 options + timer)
  timerSeconds: number; // e.g. 15s per question in expert/timer mode
}

export interface UserProgress {
  score: number;
  streak: number;
  bestStreak: number;
  totalAnswered: number;
  correctAnswers: number;
  masteredWordIds: number[];
  favoriteWordIds: number[];
  mistakeWordIds: number[];
  levelProgress: Record<CEFRLevel, { answered: number; correct: number }>;
}

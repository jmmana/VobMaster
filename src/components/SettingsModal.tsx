import React from 'react';
import { GameSettings, CategoryItem } from '../types';
import { audioService } from '../services/audioService';
import { 
  X, 
  Settings, 
  Volume2, 
  Gauge, 
  Globe2, 
  Sparkles,
  Sliders
} from 'lucide-react';

interface SettingsModalProps {
  isOpen: boolean;
  onClose: () => void;
  settings: GameSettings;
  onUpdateSettings: (updater: (prev: GameSettings) => GameSettings) => void;
  categories: CategoryItem[];
}

export const SettingsModal: React.FC<SettingsModalProps> = ({
  isOpen,
  onClose,
  settings,
  onUpdateSettings,
  categories
}) => {
  if (!isOpen) return null;

  const handleTestVoice = (accent: 'US' | 'UK' | 'AU') => {
    audioService.speak('Welcome to VocabMaster! Learning English with images and audio.', {
      accent,
      rate: settings.speechRate
    });
  };

  return (
    <div className="fixed inset-0 bg-black/80 backdrop-blur-sm flex items-center justify-center p-4 z-50 animate-in fade-in">
      <div className="bg-slate-900 border border-slate-800 rounded-3xl max-w-lg w-full p-6 sm:p-8 flex flex-col gap-6 shadow-2xl relative max-h-[90vh] overflow-y-auto">
        {/* Header */}
        <div className="flex items-center justify-between border-b border-slate-800 pb-4">
          <div className="flex items-center gap-2.5">
            <Settings className="w-6 h-6 text-emerald-400" />
            <h3 className="text-xl font-bold text-white">Configuración del Juego</h3>
          </div>
          <button
            onClick={onClose}
            className="p-1 rounded-full text-slate-400 hover:text-white hover:bg-slate-800 cursor-pointer"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Voice Accent Picker */}
        <div className="flex flex-col gap-2">
          <label className="text-xs font-bold uppercase tracking-wider text-slate-400 flex items-center gap-1.5">
            <Globe2 className="w-4 h-4 text-sky-400" />
            <span>Acento de Pronunciación en Inglés</span>
          </label>
          <div className="grid grid-cols-3 gap-2">
            {(['US', 'UK', 'AU'] as const).map((accent) => (
              <button
                key={accent}
                onClick={() => {
                  onUpdateSettings((prev) => ({ ...prev, voiceAccent: accent }));
                  handleTestVoice(accent);
                }}
                className={`py-3 px-3 rounded-2xl text-center border font-bold text-xs transition-all cursor-pointer ${
                  settings.voiceAccent === accent
                    ? 'bg-emerald-500/20 text-emerald-300 border-emerald-500 ring-2 ring-emerald-500/30'
                    : 'bg-slate-800/80 text-slate-300 border-slate-700 hover:border-slate-600'
                }`}
              >
                <div className="text-sm">{accent === 'US' ? '🇺🇸 EE.UU.' : accent === 'UK' ? '🇬🇧 Británico' : '🇦🇺 Australiano'}</div>
                <div className="text-[10px] text-slate-400 mt-0.5">Probar voz</div>
              </button>
            ))}
          </div>
        </div>

        {/* Speech Rate Slider */}
        <div className="flex flex-col gap-2">
          <div className="flex items-center justify-between">
            <label className="text-xs font-bold uppercase tracking-wider text-slate-400 flex items-center gap-1.5">
              <Gauge className="w-4 h-4 text-amber-400" />
              <span>Velocidad de Audio</span>
            </label>
            <span className="text-xs font-bold text-emerald-400">{settings.speechRate.toFixed(2)}x</span>
          </div>
          <input
            type="range"
            min="0.75"
            max="1.25"
            step="0.05"
            value={settings.speechRate}
            onChange={(e) =>
              onUpdateSettings((prev) => ({ ...prev, speechRate: parseFloat(e.target.value) }))
            }
            className="w-full accent-emerald-500 cursor-pointer"
          />
          <div className="flex justify-between text-[10px] text-slate-500">
            <span>Lento (0.75x)</span>
            <span>Normal (1.0x)</span>
            <span>Rápido (1.25x)</span>
          </div>
        </div>

        {/* Quiz Difficulty Level */}
        <div className="flex flex-col gap-2 pt-2 border-t border-slate-800">
          <label className="text-xs font-bold uppercase tracking-wider text-slate-400 flex items-center gap-1.5">
            <Sliders className="w-4 h-4 text-emerald-400" />
            <span>Dificultad del Reto / Quiz</span>
          </label>
          <div className="grid grid-cols-3 gap-2">
            {[
              { id: 'normal', name: 'Normal', desc: '4 opciones', icon: '⚡' },
              { id: 'hard', name: 'Difícil', desc: '6 opciones', icon: '🔥' },
              { id: 'expert', name: 'Experto', desc: '6 opc + 15s', icon: '⏱️' }
            ].map((diff) => (
              <button
                key={diff.id}
                type="button"
                onClick={() =>
                  onUpdateSettings((prev) => ({ ...prev, quizDifficulty: diff.id as any }))
                }
                className={`py-2.5 px-2 rounded-2xl text-center border font-bold text-xs transition-all cursor-pointer ${
                  settings.quizDifficulty === diff.id
                    ? 'bg-emerald-500/20 text-emerald-300 border-emerald-500 ring-2 ring-emerald-500/30'
                    : 'bg-slate-800/80 text-slate-300 border-slate-700 hover:border-slate-600'
                }`}
              >
                <div className="text-sm">{diff.icon} {diff.name}</div>
                <div className="text-[10px] text-slate-400 mt-0.5">{diff.desc}</div>
              </button>
            ))}
          </div>
          <p className="text-[11px] text-slate-400">
            {settings.quizDifficulty === 'normal' && 'Estándar: 4 opciones para responder a tu propio ritmo.'}
            {settings.quizDifficulty === 'hard' && 'Desafío alto: 6 opciones similares aumentan la exigencia de memoria.'}
            {settings.quizDifficulty === 'expert' && 'Extremo: 6 opciones con temporizador de 15 segundos por palabra.'}
          </p>
        </div>

        {/* Toggles */}
        <div className="flex flex-col gap-3 pt-2 border-t border-slate-800">
          {/* Auto play toggle */}
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-semibold text-white">Reproducir audio automáticamente</p>
              <p className="text-xs text-slate-400">Escuchar la palabra al cargar cada pregunta</p>
            </div>
            <input
              type="checkbox"
              checked={settings.autoPlayAudio}
              onChange={(e) =>
                onUpdateSettings((prev) => ({ ...prev, autoPlayAudio: e.target.checked }))
              }
              className="w-5 h-5 accent-emerald-500 rounded cursor-pointer"
            />
          </div>

          {/* Sound Effects toggle */}
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-semibold text-white">Efectos de sonido (SFX)</p>
              <p className="text-xs text-slate-400">Campanas de acierto, avisos y fanfarrias</p>
            </div>
            <input
              type="checkbox"
              checked={settings.soundEffects}
              onChange={(e) =>
                onUpdateSettings((prev) => ({ ...prev, soundEffects: e.target.checked }))
              }
              className="w-5 h-5 accent-emerald-500 rounded cursor-pointer"
            />
          </div>
        </div>

        {/* Close Button */}
        <button
          onClick={onClose}
          type="button"
          className="w-full py-3 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-sm cursor-pointer shadow-lg mt-2"
        >
          Guardar y Cerrar
        </button>
      </div>
    </div>
  );
};

import React, { useState } from 'react';
import { Volume2, VolumeX, Gauge } from 'lucide-react';
import { audioService } from '../services/audioService';

interface AudioPlayerButtonProps {
  text: string;
  size?: 'sm' | 'md' | 'lg' | 'hero';
  accent?: 'US' | 'UK' | 'AU';
  rate?: number;
  label?: string;
  className?: string;
  autoPlay?: boolean;
}

export const AudioPlayerButton: React.FC<AudioPlayerButtonProps> = ({
  text,
  size = 'md',
  accent = 'US',
  rate = 0.95,
  label,
  className = '',
  autoPlay = false
}) => {
  const [isPlaying, setIsPlaying] = useState(false);
  const [isSlow, setIsSlow] = useState(false);

  React.useEffect(() => {
    if (autoPlay && text) {
      handlePlay();
    }
  }, [text, autoPlay]);

  const handlePlay = async (e?: React.MouseEvent) => {
    if (e) {
      e.stopPropagation();
    }
    if (isPlaying) return;

    setIsPlaying(true);
    audioService.playClickSound();

    const actualRate = isSlow ? 0.75 : rate;
    await audioService.speak(text, { rate: actualRate, accent });
    setIsPlaying(false);
  };

  const toggleSpeed = (e: React.MouseEvent) => {
    e.stopPropagation();
    setIsSlow(!isSlow);
    audioService.playClickSound();
  };

  // Dimensions
  const sizeMap = {
    sm: 'p-2 text-sm',
    md: 'px-4 py-2.5 text-base',
    lg: 'px-6 py-3.5 text-lg',
    hero: 'px-8 py-5 text-xl font-bold'
  };

  const iconSizes = {
    sm: 'w-4 h-4',
    md: 'w-5 h-5',
    lg: 'w-6 h-6',
    hero: 'w-8 h-8'
  };

  return (
    <div className={`inline-flex items-center gap-2 ${className}`}>
      <button
        onClick={handlePlay}
        disabled={isPlaying}
        type="button"
        title="Escuchar pronunciación"
        className={`group relative inline-flex items-center justify-center gap-2.5 rounded-full font-semibold transition-all duration-200 active:scale-95 shadow-md ${
          isPlaying
            ? 'bg-emerald-500 text-white shadow-emerald-500/30 ring-4 ring-emerald-400/30 animate-pulse'
            : 'bg-emerald-600 hover:bg-emerald-500 text-white shadow-emerald-950/40 hover:shadow-emerald-500/25 cursor-pointer'
        } ${sizeMap[size]}`}
      >
        <Volume2
          className={`${iconSizes[size]} transition-transform duration-200 ${
            isPlaying ? 'scale-110' : 'group-hover:scale-110'
          }`}
        />
        {label && <span>{label}</span>}

        {/* Pulse wave indicators */}
        {isPlaying && (
          <span className="flex h-2 w-2 relative">
            <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-white opacity-75" />
            <span className="relative inline-flex rounded-full h-2 w-2 bg-white" />
          </span>
        )}
      </button>

      {/* Speed slow toggle for learners */}
      {size !== 'sm' && (
        <button
          onClick={toggleSpeed}
          type="button"
          title={isSlow ? 'Velocidad lenta activa (0.75x)' : 'Cambiar a pronunciación lenta (0.75x)'}
          className={`flex items-center gap-1 px-2.5 py-1.5 rounded-full text-xs font-medium border transition-colors cursor-pointer ${
            isSlow
              ? 'bg-amber-500/20 text-amber-300 border-amber-500/40'
              : 'bg-slate-800/80 hover:bg-slate-700 text-slate-300 border-slate-700'
          }`}
        >
          <Gauge className="w-3.5 h-3.5" />
          <span>{isSlow ? 'Lento (0.75x)' : '1.0x'}</span>
        </button>
      )}
    </div>
  );
};

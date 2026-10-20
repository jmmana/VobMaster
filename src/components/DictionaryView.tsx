import React, { useState, useMemo } from 'react';
import { WordItem, CategoryItem, CEFRLevel, UserProgress } from '../types';
import { AudioPlayerButton } from './AudioPlayerButton';
import { WordIllustration } from './WordIllustration';
import { 
  Search, 
  Filter, 
  Star, 
  Volume2, 
  CheckCircle, 
  Bookmark, 
  BookOpen, 
  Sparkles,
  ChevronLeft,
  ChevronRight
} from 'lucide-react';

interface DictionaryViewProps {
  words: WordItem[];
  categories: CategoryItem[];
  progress: UserProgress;
  onToggleFavorite: (wordId: number) => void;
  accent: 'US' | 'UK' | 'AU';
  rate: number;
}

const ITEMS_PER_PAGE = 30;

export const DictionaryView: React.FC<DictionaryViewProps> = ({
  words,
  categories,
  progress,
  onToggleFavorite,
  accent,
  rate
}) => {
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState<string>('all');
  const [selectedLevel, setSelectedLevel] = useState<string>('all');
  const [filterFavoritesOnly, setFilterFavoritesOnly] = useState(false);
  const [currentPage, setCurrentPage] = useState(1);

  // Filter words based on search, category, level, and favorites
  const filteredWords = useMemo(() => {
    return words.filter((item) => {
      // Search filter
      if (searchQuery.trim()) {
        const query = searchQuery.toLowerCase().trim();
        const matchesWord = item.word.toLowerCase().includes(query);
        const matchesTranslation = item.translation.toLowerCase().includes(query);
        const matchesExample = item.example.toLowerCase().includes(query);
        if (!matchesWord && !matchesTranslation && !matchesExample) {
          return false;
        }
      }

      // Category filter
      if (selectedCategory !== 'all' && item.categoryId !== selectedCategory) {
        return false;
      }

      // Level filter
      if (selectedLevel !== 'all' && item.level !== selectedLevel) {
        return false;
      }

      // Favorites filter
      if (filterFavoritesOnly && !progress.favoriteWordIds.includes(item.id)) {
        return false;
      }

      return true;
    });
  }, [words, searchQuery, selectedCategory, selectedLevel, filterFavoritesOnly, progress.favoriteWordIds]);

  // Reset page when filters change
  React.useEffect(() => {
    setCurrentPage(1);
  }, [searchQuery, selectedCategory, selectedLevel, filterFavoritesOnly]);

  // Paginated subset
  const totalPages = Math.ceil(filteredWords.length / ITEMS_PER_PAGE);
  const paginatedWords = useMemo(() => {
    const start = (currentPage - 1) * ITEMS_PER_PAGE;
    return filteredWords.slice(start, start + ITEMS_PER_PAGE);
  }, [filteredWords, currentPage]);

  const levels: ('all' | CEFRLevel)[] = ['all', 'A1', 'A2', 'B1', 'B2', 'C1'];

  return (
    <div className="max-w-6xl mx-auto px-4 py-6 sm:py-8 flex flex-col gap-6">
      {/* Header Info */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-800 pb-5">
        <div>
          <h2 className="text-2xl sm:text-3xl font-extrabold text-white flex items-center gap-2.5">
            <BookOpen className="w-7 h-7 text-emerald-400" />
            <span>Diccionario Interactivo</span>
          </h2>
          <p className="text-slate-400 text-sm mt-1">
            Explora las <strong className="text-emerald-400 font-bold">{words.length} palabras</strong> con audio nativo, imágenes y ejemplos.
          </p>
        </div>

        {/* Total found badge */}
        <div className="flex items-center gap-2">
          <span className="px-3 py-1.5 rounded-full bg-slate-800 text-slate-300 text-xs font-semibold border border-slate-700">
            Mostrando <strong>{filteredWords.length}</strong> de {words.length}
          </span>
          <button
            type="button"
            onClick={() => setFilterFavoritesOnly(!filterFavoritesOnly)}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-full text-xs font-semibold border transition-colors cursor-pointer ${
              filterFavoritesOnly
                ? 'bg-amber-500/20 text-amber-300 border-amber-500/40'
                : 'bg-slate-800/80 hover:bg-slate-700 text-slate-300 border-slate-700'
            }`}
          >
            <Star className={`w-3.5 h-3.5 ${filterFavoritesOnly ? 'fill-amber-400 text-amber-400' : ''}`} />
            <span>Favoritas ({progress.favoriteWordIds.length})</span>
          </button>
        </div>
      </div>

      {/* Search Bar & Level Selector */}
      <div className="grid grid-cols-1 md:grid-cols-12 gap-3">
        {/* Search input */}
        <div className="md:col-span-8 relative">
          <Search className="w-5 h-5 absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400" />
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="Buscar en inglés o español (ej: butterfly, manzana, walk, happy)..."
            className="w-full pl-11 pr-4 py-3 rounded-2xl bg-slate-900 border border-slate-800 text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-emerald-500/50 text-sm transition-all"
          />
          {searchQuery && (
            <button
              onClick={() => setSearchQuery('')}
              className="absolute right-3.5 top-1/2 -translate-y-1/2 text-xs text-slate-400 hover:text-white"
            >
              Limpiar
            </button>
          )}
        </div>

        {/* Level filter tabs */}
        <div className="md:col-span-4 flex items-center justify-between sm:justify-start gap-1 p-1 rounded-2xl bg-slate-900 border border-slate-800">
          {levels.map((lvl) => (
            <button
              key={lvl}
              onClick={() => setSelectedLevel(lvl)}
              className={`flex-1 py-2 text-xs font-bold rounded-xl transition-all cursor-pointer ${
                selectedLevel === lvl
                  ? 'bg-emerald-500 text-white shadow-sm'
                  : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800'
              }`}
            >
              {lvl === 'all' ? 'Todos' : lvl}
            </button>
          ))}
        </div>
      </div>

      {/* Category Horizontal Carousel */}
      <div className="flex items-center gap-2 overflow-x-auto pb-2 scrollbar-thin scrollbar-thumb-slate-800">
        <button
          onClick={() => setSelectedCategory('all')}
          className={`flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs font-semibold shrink-0 border transition-all cursor-pointer ${
            selectedCategory === 'all'
              ? 'bg-emerald-500 text-white border-emerald-400 shadow-md shadow-emerald-950/40'
              : 'bg-slate-900/90 text-slate-400 border-slate-800 hover:text-slate-200 hover:border-slate-700'
          }`}
        >
          <span>✨ Todas las categorías</span>
          <span className="opacity-70">({words.length})</span>
        </button>

        {categories.map((cat) => (
          <button
            key={cat.id}
            onClick={() => setSelectedCategory(cat.id)}
            className={`flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs font-semibold shrink-0 border transition-all cursor-pointer ${
              selectedCategory === cat.id
                ? 'bg-emerald-500 text-white border-emerald-400 shadow-md shadow-emerald-950/40'
                : 'bg-slate-900/90 text-slate-400 border-slate-800 hover:text-slate-200 hover:border-slate-700'
            }`}
          >
            <span>{cat.emoji}</span>
            <span>{cat.name}</span>
            <span className="opacity-60 text-[10px]">({cat.count})</span>
          </button>
        ))}
      </div>

      {/* Words Grid Display */}
      {paginatedWords.length === 0 ? (
        <div className="text-center py-16 px-4 bg-slate-900/40 rounded-3xl border border-slate-800 flex flex-col items-center gap-3">
          <Search className="w-10 h-10 text-slate-600" />
          <h4 className="text-lg font-bold text-slate-300">No se encontraron palabras</h4>
          <p className="text-sm text-slate-500 max-w-sm">
            Prueba ajustando los filtros de búsqueda, categoría o nivel para explorar el diccionario.
          </p>
        </div>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {paginatedWords.map((word) => {
            const isFav = progress.favoriteWordIds.includes(word.id);
            const isMastered = progress.masteredWordIds.includes(word.id);

            return (
              <div
                key={word.id}
                className="bg-slate-900/80 backdrop-blur-sm rounded-2xl border border-slate-800/90 p-4 flex flex-col justify-between hover:border-slate-700 transition-all hover:shadow-xl group"
              >
                <div>
                  {/* Top Bar: Illustration preview + Badges */}
                  <div className="flex items-start gap-3 mb-3">
                    <div className="w-16 h-16 shrink-0 rounded-xl overflow-hidden shadow-md">
                      <WordIllustration word={word} size="sm" showDetails={false} />
                    </div>

                    <div className="flex-1 min-w-0">
                      <div className="flex items-center justify-between gap-1">
                        <span className="px-2 py-0.5 text-[10px] font-bold rounded-full bg-slate-800 text-slate-300 border border-slate-700 uppercase">
                          {word.level}
                        </span>

                        <button
                          type="button"
                          onClick={() => onToggleFavorite(word.id)}
                          className="p-1 rounded-full text-slate-400 hover:text-amber-400 transition-colors cursor-pointer"
                          title={isFav ? 'Quitar de favoritas' : 'Guardar en favoritas'}
                        >
                          <Star className={`w-4 h-4 ${isFav ? 'fill-amber-400 text-amber-400' : ''}`} />
                        </button>
                      </div>

                      <h3 className="text-lg font-bold text-white truncate capitalize mt-1">
                        {word.word}
                      </h3>
                      <p className="text-slate-400 text-xs font-mono">
                        {word.phonetic}
                      </p>
                    </div>
                  </div>

                  {/* Spanish Translation */}
                  <div className="bg-slate-800/40 rounded-xl px-3 py-2 border border-slate-800/60 mb-3">
                    <span className="text-xs text-slate-400 block font-medium">Traducción:</span>
                    <span className="text-sm font-semibold text-emerald-300 capitalize">
                      {word.translation}
                    </span>
                  </div>

                  {/* Context Sentence */}
                  <div className="text-xs text-slate-300 border-l-2 border-emerald-500/60 pl-2.5 py-0.5 mb-3 italic">
                    "{word.example}"
                  </div>
                </div>

                {/* Bottom Actions: Audio Pronunciation */}
                <div className="flex items-center justify-between pt-2 border-t border-slate-800/80">
                  <span className="text-[11px] text-slate-500">
                    {word.category}
                  </span>

                  <AudioPlayerButton
                    text={word.word}
                    size="sm"
                    accent={accent}
                    rate={rate}
                    label="Pronunciar"
                  />
                </div>
              </div>
            );
          })}
        </div>
      )}

      {/* Pagination Controls */}
      {totalPages > 1 && (
        <div className="flex items-center justify-between border-t border-slate-800 pt-5">
          <p className="text-xs text-slate-400">
            Página <strong>{currentPage}</strong> de {totalPages}
          </p>

          <div className="flex items-center gap-2">
            <button
              onClick={() => setCurrentPage((p) => Math.max(1, p - 1))}
              disabled={currentPage === 1}
              className="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 disabled:opacity-30 disabled:pointer-events-none text-slate-200 cursor-pointer"
            >
              <ChevronLeft className="w-5 h-5" />
            </button>
            <button
              onClick={() => setCurrentPage((p) => Math.min(totalPages, p + 1))}
              disabled={currentPage === totalPages}
              className="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 disabled:opacity-30 disabled:pointer-events-none text-slate-200 cursor-pointer"
            >
              <ChevronRight className="w-5 h-5" />
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

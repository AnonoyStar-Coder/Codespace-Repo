import { X } from 'lucide-react';

interface AiSuggestionsProps {
  loading: boolean;
  suggestions: string[];
  onSelect: (suggestion: string) => void;
  onClose: () => void;
}

const AiSuggestions = ({ loading, suggestions, onSelect, onClose }: AiSuggestionsProps) => {
  return (
    <div className="mt-4 bg-indigo-50 border border-indigo-200 rounded-lg p-4 relative">
      <button
        onClick={onClose}
        className="absolute top-2 right-2 text-gray-500 hover:text-gray-700"
      >
        <X className="h-5 w-5" />
      </button>
      
      <h4 className="text-indigo-800 font-medium mb-3 flex items-center">
        <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-2" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
          <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2z"></path>
          <path d="M16 14l-4-4-4 4"></path>
        </svg>
        AI Suggestions
      </h4>
      
      {loading ? (
        <div className="flex justify-center items-center py-4">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-indigo-700"></div>
        </div>
      ) : suggestions.length === 0 ? (
        <p className="text-gray-600 italic">No suggestions available. Try providing more context.</p>
      ) : (
        <ul className="space-y-2">
          {suggestions.map((suggestion, index) => (
            <li key={index}>
              <button
                onClick={() => onSelect(suggestion)}
                className="w-full text-left p-3 rounded-md bg-white border border-indigo-100 hover:bg-indigo-100 transition-colors"
              >
                {suggestion}
              </button>
            </li>
          ))}
        </ul>
      )}
      
      <p className="text-xs text-gray-500 mt-3">
        Click on any suggestion to use it in your resume. These are AI-generated recommendations based on your input.
      </p>
    </div>
  );
};

export default AiSuggestions;
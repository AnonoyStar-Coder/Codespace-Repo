import { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { FileText, Menu, X } from 'lucide-react';

const Navbar = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const location = useLocation();

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  return (
    <header className="bg-white shadow-sm fixed w-full top-0 z-50">
      <div className="container mx-auto px-4">
        <div className="flex items-center justify-between h-16">
          <div className="flex items-center">
            <Link to="/" className="flex items-center">
              <FileText className="h-8 w-8 text-blue-500" />
              <span className="ml-2 text-xl font-bold text-gray-900">AI Resume Builder</span>
            </Link>
          </div>
          
          {/* Desktop menu */}
          <nav className="hidden md:flex items-center space-x-8">
            <Link 
              to="/"
              className={`text-sm font-medium ${
                location.pathname === '/' 
                  ? 'text-blue-600 border-b-2 border-blue-500' 
                  : 'text-gray-700 hover:text-blue-500'
              }`}
            >
              Home
            </Link>
            <Link 
              to="/builder"
              className={`text-sm font-medium ${
                location.pathname === '/builder' 
                  ? 'text-blue-600 border-b-2 border-blue-500' 
                  : 'text-gray-700 hover:text-blue-500'
              }`}
            >
              Builder
            </Link>
            <Link 
              to="/preview"
              className={`text-sm font-medium ${
                location.pathname === '/preview' 
                  ? 'text-blue-600 border-b-2 border-blue-500' 
                  : 'text-gray-700 hover:text-blue-500'
              }`}
            >
              Preview
            </Link>
          </nav>

          {/* Mobile menu button */}
          <div className="md:hidden">
            <button
              type="button"
              className="text-gray-500 hover:text-gray-700 focus:outline-none"
              onClick={toggleMenu}
            >
              {isMenuOpen ? (
                <X className="h-6 w-6" />
              ) : (
                <Menu className="h-6 w-6" />
              )}
            </button>
          </div>
        </div>
      </div>

      {/* Mobile menu */}
      {isMenuOpen && (
        <div className="md:hidden border-t border-gray-200 bg-white">
          <div className="container mx-auto px-4 py-3 space-y-3">
            <Link 
              to="/"
              className={`block text-sm font-medium ${
                location.pathname === '/' 
                  ? 'text-blue-600' 
                  : 'text-gray-700 hover:text-blue-500'
              }`}
              onClick={() => setIsMenuOpen(false)}
            >
              Home
            </Link>
            <Link 
              to="/builder"
              className={`block text-sm font-medium ${
                location.pathname === '/builder' 
                  ? 'text-blue-600' 
                  : 'text-gray-700 hover:text-blue-500'
              }`}
              onClick={() => setIsMenuOpen(false)}
            >
              Builder
            </Link>
            <Link 
              to="/preview"
              className={`block text-sm font-medium ${
                location.pathname === '/preview' 
                  ? 'text-blue-600' 
                  : 'text-gray-700 hover:text-blue-500'
              }`}
              onClick={() => setIsMenuOpen(false)}
            >
              Preview
            </Link>
          </div>
        </div>
      )}
    </header>
  );
};

export default Navbar;
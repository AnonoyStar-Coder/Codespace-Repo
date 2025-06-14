import { Routes, Route } from 'react-router-dom';
import HomePage from './pages/HomePage';
import ResumeBuilder from './pages/ResumeBuilder';
import ResumePreview from './pages/ResumePreview';
import Navbar from './components/Navbar';
import { ResumeProvider } from './context/ResumeContext';

function App() {
  return (
    <ResumeProvider>
      <div className="min-h-screen bg-gray-50 flex flex-col">
        <Navbar />
        <main className="flex-grow">
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/builder" element={<ResumeBuilder />} />
            <Route path="/preview" element={<ResumePreview />} />
          </Routes>
        </main>
        <footer className="py-6 bg-white border-t border-gray-200">
          <div className="container mx-auto px-4 text-center text-gray-500 text-sm">
            © {new Date().getFullYear()} AI Resume Builder. All rights reserved.
          </div>
        </footer>
      </div>
    </ResumeProvider>
  );
}

export default App;
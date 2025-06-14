import { useEffect } from 'react';
import { Link } from 'react-router-dom';
import { FileText, Sparkles, Download, Zap } from 'lucide-react';

const HomePage = () => {
  useEffect(() => {
    // Add smooth scrolling for internal links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href') as string);
        if (target) {
          target.scrollIntoView({ behavior: 'smooth' });
        }
      });
    });
  }, []);

  return (
    <div className="pt-16">
      {/* Hero section */}
      <section className="relative bg-gradient-to-r from-blue-600 to-indigo-700 text-white">
        <div className="absolute inset-0 bg-pattern opacity-10"></div>
        <div className="container mx-auto px-4 py-20 md:py-32 relative z-10">
          <div className="max-w-3xl mx-auto text-center">
            <h1 className="text-4xl md:text-5xl font-bold mb-6 leading-tight animate-fade-in">
              Create Professional Resumes with AI Assistance
            </h1>
            <p className="text-xl md:text-2xl mb-10 text-blue-100 animate-slide-up">
              Build standout resumes easily with our intelligent resume builder powered by AI technologies
            </p>
            <div className="flex flex-col sm:flex-row justify-center gap-4 animate-fade-in" style={{ animationDelay: '0.3s' }}>
              <Link to="/builder" className="btn-primary bg-white text-blue-700 hover:bg-blue-50 py-3 px-8 rounded-lg font-semibold text-lg transition-all transform hover:scale-105">
                Build Your Resume
              </Link>
              <a href="#features" className="btn-secondary bg-transparent border-2 border-white py-3 px-8 rounded-lg font-semibold text-lg hover:bg-white/10 transition-all">
                Learn More
              </a>
            </div>
          </div>
        </div>
        <div className="absolute bottom-0 left-0 right-0 h-16 bg-gradient-to-t from-white to-transparent"></div>
      </section>

      {/* Features section */}
      <section id="features" className="py-20 bg-white">
        <div className="container mx-auto px-4">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold mb-4 text-gray-900">Powerful Features</h2>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto">Our AI-powered resume builder helps you create professional resumes in minutes</p>
          </div>
          
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            <div className="bg-white p-8 rounded-xl shadow-sm border border-gray-100 hover:shadow-md transition-all">
              <div className="inline-block p-3 bg-blue-100 rounded-lg text-blue-600 mb-4">
                <Sparkles className="h-6 w-6" />
              </div>
              <h3 className="text-xl font-semibold mb-3 text-gray-900">AI Powered Suggestions</h3>
              <p className="text-gray-600">Get intelligent content suggestions based on your experience and skills to make your resume stand out.</p>
            </div>
            
            <div className="bg-white p-8 rounded-xl shadow-sm border border-gray-100 hover:shadow-md transition-all">
              <div className="inline-block p-3 bg-purple-100 rounded-lg text-purple-600 mb-4">
                <FileText className="h-6 w-6" />
              </div>
              <h3 className="text-xl font-semibold mb-3 text-gray-900">Professional Templates</h3>
              <p className="text-gray-600">Choose from a variety of professionally designed resume templates suitable for any industry.</p>
            </div>
            
            <div className="bg-white p-8 rounded-xl shadow-sm border border-gray-100 hover:shadow-md transition-all">
              <div className="inline-block p-3 bg-green-100 rounded-lg text-green-600 mb-4">
                <Download className="h-6 w-6" />
              </div>
              <h3 className="text-xl font-semibold mb-3 text-gray-900">Easy Export</h3>
              <p className="text-gray-600">Export your resume as a PDF file with a single click, ready to be sent to potential employers.</p>
            </div>
            
            <div className="bg-white p-8 rounded-xl shadow-sm border border-gray-100 hover:shadow-md transition-all">
              <div className="inline-block p-3 bg-yellow-100 rounded-lg text-yellow-600 mb-4">
                <Zap className="h-6 w-6" />
              </div>
              <h3 className="text-xl font-semibold mb-3 text-gray-900">Real-time Preview</h3>
              <p className="text-gray-600">See changes to your resume in real-time as you edit, giving you complete control over your content.</p>
            </div>
            
            <div className="bg-white p-8 rounded-xl shadow-sm border border-gray-100 hover:shadow-md transition-all">
              <div className="inline-block p-3 bg-red-100 rounded-lg text-red-600 mb-4">
                <svg className="h-6 w-6" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                  <path d="M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10z"></path>
                  <path d="m7 10 2 2 6-6"></path>
                </svg>
              </div>
              <h3 className="text-xl font-semibold mb-3 text-gray-900">Auto-save</h3>
              <p className="text-gray-600">Your progress is automatically saved, so you never have to worry about losing your work.</p>
            </div>
            
            <div className="bg-white p-8 rounded-xl shadow-sm border border-gray-100 hover:shadow-md transition-all">
              <div className="inline-block p-3 bg-indigo-100 rounded-lg text-indigo-600 mb-4">
                <svg className="h-6 w-6" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                  <rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect>
                  <line x1="8" y1="21" x2="16" y2="21"></line>
                  <line x1="12" y1="17" x2="12" y2="21"></line>
                </svg>
              </div>
              <h3 className="text-xl font-semibold mb-3 text-gray-900">Mobile Friendly</h3>
              <p className="text-gray-600">Build and edit your resume on any device, from desktop to smartphone with our responsive design.</p>
            </div>
          </div>
        </div>
      </section>

      {/* CTA section */}
      <section className="py-20 bg-gray-50">
        <div className="container mx-auto px-4 text-center">
          <h2 className="text-3xl md:text-4xl font-bold mb-6 text-gray-900">Ready to Create Your Professional Resume?</h2>
          <p className="text-xl text-gray-600 mb-10 max-w-3xl mx-auto">Get started today and create a resume that stands out. Our AI-powered builder makes it easy to craft the perfect resume.</p>
          <Link to="/builder" className="inline-block bg-blue-600 hover:bg-blue-700 text-white py-3 px-8 rounded-lg font-semibold text-lg transition-colors">
            Start Building Now
          </Link>
        </div>
      </section>
    </div>
  );
};

export default HomePage;
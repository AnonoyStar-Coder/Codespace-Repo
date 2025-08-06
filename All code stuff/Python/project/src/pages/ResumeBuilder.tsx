import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useResume } from '../context/ResumeContext';
import PersonalInfoForm from '../components/forms/PersonalInfoForm';
import ExperienceForm from '../components/forms/ExperienceForm';
import EducationForm from '../components/forms/EducationForm';
import SkillsForm from '../components/forms/SkillsForm';
import ProjectsForm from '../components/forms/ProjectsForm';
import TemplateSelector from '../components/TemplateSelector';
import ResumePreviewPane from '../components/preview/ResumePreviewPane';
import { Save, Eye } from 'lucide-react';

const ResumeBuilder = () => {
  const { resume, loading, saving, saveResume } = useResume();
  const [activeSection, setActiveSection] = useState('personal');
  const [showPreview, setShowPreview] = useState(false);
  const [lastSaved, setLastSaved] = useState<Date | null>(null);
  const navigate = useNavigate();

  // Auto-save timer
  useEffect(() => {
    const timer = setTimeout(() => {
      if (resume && Object.keys(resume.personal).length > 0) {
        handleSave();
      }
    }, 30000); // Save every 30 seconds

    return () => clearTimeout(timer);
  }, [resume]);

  const handleSave = async () => {
    await saveResume();
    setLastSaved(new Date());
  };

  const togglePreview = () => {
    setShowPreview(!showPreview);
  };

  const handlePreviewClick = () => {
    saveResume().then(() => {
      navigate('/preview');
    });
  };

  const sections = [
    { id: 'personal', label: 'Personal Info' },
    { id: 'experience', label: 'Experience' },
    { id: 'education', label: 'Education' },
    { id: 'skills', label: 'Skills' },
    { id: 'projects', label: 'Projects' },
    { id: 'templates', label: 'Templates' }
  ];

  if (loading) {
    return (
      <div className="h-screen flex items-center justify-center pt-16">
        <div className="loading-spinner"></div>
      </div>
    );
  }

  return (
    <div className="container mx-auto pt-20 pb-8 px-4">
      <div className="flex flex-col lg:flex-row gap-6">
        {/* Left Side - Form */}
        <div className={`${showPreview ? 'hidden lg:block' : ''} lg:w-1/2 transition-all`}>
          <div className="bg-white rounded-lg shadow-sm mb-6">
            <div className="border-b border-gray-200">
              <nav className="flex overflow-x-auto">
                {sections.map((section) => (
                  <button
                    key={section.id}
                    onClick={() => setActiveSection(section.id)}
                    className={`px-4 py-3 text-sm font-medium whitespace-nowrap ${
                      activeSection === section.id
                        ? 'border-b-2 border-blue-500 text-blue-600'
                        : 'text-gray-600 hover:text-gray-900'
                    }`}
                  >
                    {section.label}
                  </button>
                ))}
              </nav>
            </div>

            <div className="p-6">
              {activeSection === 'personal' && <PersonalInfoForm />}
              {activeSection === 'experience' && <ExperienceForm />}
              {activeSection === 'education' && <EducationForm />}
              {activeSection === 'skills' && <SkillsForm />}
              {activeSection === 'projects' && <ProjectsForm />}
              {activeSection === 'templates' && <TemplateSelector />}
            </div>
          </div>

          <div className="flex items-center justify-between bg-white rounded-lg shadow-sm p-4">
            <div>
              {lastSaved && (
                <span className="text-sm text-gray-500">
                  Last saved: {lastSaved.toLocaleTimeString()}
                </span>
              )}
            </div>
            <div className="flex gap-3">
              <button
                onClick={handleSave}
                disabled={saving}
                className="flex items-center gap-2 px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition-colors disabled:opacity-70"
              >
                <Save className="w-4 h-4" />
                {saving ? 'Saving...' : 'Save'}
              </button>
              <button
                onClick={handlePreviewClick}
                className="flex items-center gap-2 px-4 py-2 bg-gray-800 text-white rounded-md hover:bg-gray-900 transition-colors"
              >
                <Eye className="w-4 h-4" />
                Preview
              </button>
            </div>
          </div>
        </div>

        {/* Right Side - Preview */}
        <div className={`${!showPreview ? 'hidden lg:block' : ''} lg:w-1/2 transition-all`}>
          <div className="sticky top-24">
            <div className="bg-white rounded-lg shadow-sm p-6">
              <h2 className="text-xl font-semibold mb-4 text-gray-800">Live Preview</h2>
              <div className="bg-gray-100 p-4 rounded-md mb-4 overflow-hidden">
                <ResumePreviewPane />
              </div>
            </div>
          </div>
        </div>

        {/* Mobile Preview Toggle */}
        <button
          className="fixed bottom-6 right-6 lg:hidden z-20 bg-blue-600 text-white p-4 rounded-full shadow-lg"
          onClick={togglePreview}
        >
          <Eye className="h-6 w-6" />
        </button>
      </div>
    </div>
  );
};

export default ResumeBuilder;
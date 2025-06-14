import { useState, useEffect } from 'react';
import { useResume } from '../context/ResumeContext';
import { Check } from 'lucide-react';

const templates = [
  {
    id: 'modern',
    name: 'Modern',
    description: 'Clean and professional template with a modern design',
    thumbnail: 'https://images.pexels.com/photos/590016/pexels-photo-590016.jpeg?auto=compress&cs=tinysrgb&w=300'
  },
  {
    id: 'classic',
    name: 'Classic',
    description: 'Traditional resume format that works for any industry',
    thumbnail: 'https://images.pexels.com/photos/590022/pexels-photo-590022.jpeg?auto=compress&cs=tinysrgb&w=300'
  },
  {
    id: 'creative',
    name: 'Creative',
    description: 'Bold design for creative professionals',
    thumbnail: 'https://images.pexels.com/photos/590045/pexels-photo-590045.jpeg?auto=compress&cs=tinysrgb&w=300'
  },
  {
    id: 'minimal',
    name: 'Minimal',
    description: 'Simple and elegant design that focuses on content',
    thumbnail: 'https://images.pexels.com/photos/590029/pexels-photo-590029.jpeg?auto=compress&cs=tinysrgb&w=300'
  }
];

const TemplateSelector = () => {
  const { resume, changeTemplate } = useResume();
  const [selectedTemplate, setSelectedTemplate] = useState(resume.template || 'modern');

  useEffect(() => {
    setSelectedTemplate(resume.template || 'modern');
  }, [resume.template]);

  const handleTemplateChange = (templateId: string) => {
    setSelectedTemplate(templateId);
    changeTemplate(templateId);
  };

  return (
    <div className="space-y-6">
      <div>
        <h3 className="text-xl font-semibold text-gray-800 mb-4">Resume Template</h3>
        <p className="text-gray-600 mb-6">
          Choose a template that best represents your professional style.
        </p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-2 lg:grid-cols-4 gap-4">
        {templates.map((template) => (
          <div
            key={template.id}
            onClick={() => handleTemplateChange(template.id)}
            className={`cursor-pointer rounded-lg overflow-hidden border-2 transition-all ${
              selectedTemplate === template.id
                ? 'border-blue-500 shadow-md transform scale-[1.02]'
                : 'border-gray-200 hover:border-gray-300'
            }`}
          >
            <div className="relative h-40 bg-gray-100">
              <img
                src={template.thumbnail}
                alt={template.name}
                className="w-full h-full object-cover"
              />
              {selectedTemplate === template.id && (
                <div className="absolute top-2 right-2 bg-blue-500 text-white p-1 rounded-full">
                  <Check className="h-4 w-4" />
                </div>
              )}
            </div>
            <div className="p-3">
              <h4 className="font-medium text-gray-900">{template.name}</h4>
              <p className="text-sm text-gray-500">{template.description}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default TemplateSelector;
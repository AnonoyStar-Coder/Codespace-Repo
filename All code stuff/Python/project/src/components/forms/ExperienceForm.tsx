import { useState } from 'react';
import { useResume } from '../../context/ResumeContext';
import { Plus, Edit, Trash, Sparkles } from 'lucide-react';
import AiSuggestions from '../AiSuggestions';

const ExperienceForm = () => {
  const { resume, addExperience, updateExperience, removeExperience, getAiSuggestions } = useResume();
  const [editMode, setEditMode] = useState<string | null>(null);
  const [showForm, setShowForm] = useState(false);
  const [showSuggestions, setShowSuggestions] = useState(false);
  const [loadingSuggestions, setLoadingSuggestions] = useState(false);
  const [suggestions, setSuggestions] = useState<string[]>([]);
  const [currentExperience, setCurrentExperience] = useState<string | null>(null);
  
  const emptyExperience = {
    id: '',
    company: '',
    position: '',
    location: '',
    startDate: '',
    endDate: '',
    current: false,
    description: ''
  };
  
  const [formData, setFormData] = useState(emptyExperience);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleCheckboxChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData(prev => ({ ...prev, current: e.target.checked }));
    if (e.target.checked) {
      setFormData(prev => ({ ...prev, endDate: '' }));
    }
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    
    if (editMode) {
      updateExperience(editMode, formData);
    } else {
      addExperience(formData);
    }
    
    setFormData(emptyExperience);
    setEditMode(null);
    setShowForm(false);
  };

  const handleEdit = (id: string) => {
    const experienceToEdit = resume.experience.find(exp => exp.id === id);
    if (experienceToEdit) {
      setFormData(experienceToEdit);
      setEditMode(id);
      setShowForm(true);
    }
  };

  const handleDelete = (id: string) => {
    if (window.confirm('Are you sure you want to delete this experience?')) {
      removeExperience(id);
    }
  };

  const handleCancel = () => {
    setFormData(emptyExperience);
    setEditMode(null);
    setShowForm(false);
  };

  const handleGetSuggestions = async (id: string) => {
    setLoadingSuggestions(true);
    setShowSuggestions(true);
    setCurrentExperience(id);
    
    try {
      const experience = resume.experience.find(exp => exp.id === id);
      if (experience) {
        const context = `Position: ${experience.position} at ${experience.company}
          Industry: ${experience.company} 
          Duration: ${experience.startDate} to ${experience.current ? 'Present' : experience.endDate}`;
        
        const result = await getAiSuggestions('experience', context);
        setSuggestions(result);
      }
    } catch (error) {
      console.error('Error getting suggestions:', error);
    } finally {
      setLoadingSuggestions(false);
    }
  };

  const applySuggestion = (suggestion: string) => {
    if (currentExperience) {
      const updatedExperience = resume.experience.find(exp => exp.id === currentExperience);
      if (updatedExperience) {
        updateExperience(currentExperience, {
          ...updatedExperience,
          description: suggestion
        });
      }
    }
    setShowSuggestions(false);
  };

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h3 className="text-xl font-semibold text-gray-800">Work Experience</h3>
        {!showForm && (
          <button
            type="button"
            onClick={() => setShowForm(true)}
            className="flex items-center text-sm px-3 py-1.5 bg-blue-100 text-blue-700 rounded-md hover:bg-blue-200 transition-colors"
          >
            <Plus className="h-4 w-4 mr-1" />
            Add Experience
          </button>
        )}
      </div>

      {/* Form for adding/editing */}
      {showForm && (
        <form onSubmit={handleSubmit} className="bg-gray-50 p-4 rounded-md mb-4">
          <h4 className="text-lg font-medium text-gray-800 mb-4">
            {editMode ? 'Edit Experience' : 'Add Experience'}
          </h4>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
            <div>
              <label htmlFor="company" className="block text-sm font-medium text-gray-700 mb-1">
                Company/Organization *
              </label>
              <input
                type="text"
                id="company"
                name="company"
                value={formData.company}
                onChange={handleChange}
                required
                className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
              />
            </div>
            
            <div>
              <label htmlFor="position" className="block text-sm font-medium text-gray-700 mb-1">
                Position/Title *
              </label>
              <input
                type="text"
                id="position"
                name="position"
                value={formData.position}
                onChange={handleChange}
                required
                className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
              />
            </div>
            
            <div>
              <label htmlFor="location" className="block text-sm font-medium text-gray-700 mb-1">
                Location
              </label>
              <input
                type="text"
                id="location"
                name="location"
                value={formData.location}
                onChange={handleChange}
                className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
              />
            </div>
            
            <div>
              <label htmlFor="startDate" className="block text-sm font-medium text-gray-700 mb-1">
                Start Date *
              </label>
              <input
                type="month"
                id="startDate"
                name="startDate"
                value={formData.startDate}
                onChange={handleChange}
                required
                className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
              />
            </div>
            
            <div className="flex items-center mb-2">
              <input
                type="checkbox"
                id="current"
                name="current"
                checked={formData.current}
                onChange={handleCheckboxChange}
                className="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
              />
              <label htmlFor="current" className="ml-2 block text-sm text-gray-700">
                I currently work here
              </label>
            </div>
            
            {!formData.current && (
              <div>
                <label htmlFor="endDate" className="block text-sm font-medium text-gray-700 mb-1">
                  End Date *
                </label>
                <input
                  type="month"
                  id="endDate"
                  name="endDate"
                  value={formData.endDate}
                  onChange={handleChange}
                  required={!formData.current}
                  disabled={formData.current}
                  className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 disabled:bg-gray-100 disabled:text-gray-500"
                />
              </div>
            )}
          </div>
          
          <div className="mb-4">
            <label htmlFor="description" className="block text-sm font-medium text-gray-700 mb-1">
              Description *
            </label>
            <textarea
              id="description"
              name="description"
              value={formData.description}
              onChange={handleChange}
              required
              rows={4}
              className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
              placeholder="Describe your responsibilities, achievements, and the skills you developed"
            ></textarea>
          </div>
          
          <div className="flex justify-end space-x-3">
            <button
              type="button"
              onClick={handleCancel}
              className="px-4 py-2 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
            >
              Cancel
            </button>
            <button
              type="submit"
              className="px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
            >
              {editMode ? 'Update' : 'Add'}
            </button>
          </div>
        </form>
      )}

      {/* List of experiences */}
      {resume.experience.length === 0 ? (
        <p className="text-gray-500 italic">No work experience added yet.</p>
      ) : (
        <div className="space-y-4">
          {resume.experience.map((exp) => (
            <div key={exp.id} className="bg-white border border-gray-200 rounded-md p-4 hover:shadow-sm transition-shadow">
              <div className="flex justify-between">
                <div>
                  <h4 className="text-lg font-medium text-gray-900">{exp.position}</h4>
                  <p className="text-gray-600">{exp.company}{exp.location ? `, ${exp.location}` : ''}</p>
                  <p className="text-sm text-gray-500">
                    {new Date(exp.startDate).toLocaleDateString('en-US', { year: 'numeric', month: 'short' })} - 
                    {exp.current 
                      ? ' Present'
                      : ` ${new Date(exp.endDate).toLocaleDateString('en-US', { year: 'numeric', month: 'short' })}`
                    }
                  </p>
                </div>
                <div className="flex space-x-2">
                  <button
                    onClick={() => handleGetSuggestions(exp.id)}
                    className="text-indigo-600 hover:text-indigo-800"
                    title="Get AI suggestions"
                  >
                    <Sparkles className="h-5 w-5" />
                  </button>
                  <button
                    onClick={() => handleEdit(exp.id)}
                    className="text-blue-600 hover:text-blue-800"
                    title="Edit"
                  >
                    <Edit className="h-5 w-5" />
                  </button>
                  <button
                    onClick={() => handleDelete(exp.id)}
                    className="text-red-600 hover:text-red-800"
                    title="Delete"
                  >
                    <Trash className="h-5 w-5" />
                  </button>
                </div>
              </div>
              <p className="mt-2 text-gray-700 whitespace-pre-line">{exp.description}</p>
            </div>
          ))}
        </div>
      )}

      {showSuggestions && (
        <AiSuggestions
          loading={loadingSuggestions}
          suggestions={suggestions}
          onSelect={applySuggestion}
          onClose={() => setShowSuggestions(false)}
        />
      )}
    </div>
  );
};

export default ExperienceForm;
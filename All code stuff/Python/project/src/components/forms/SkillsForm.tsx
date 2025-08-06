import { useState } from 'react';
import { useResume } from '../../context/ResumeContext';
import { Plus, Edit, Trash, Sparkles } from 'lucide-react';
import AiSuggestions from '../AiSuggestions';

const SkillsForm = () => {
  const { resume, addSkill, updateSkill, removeSkill, getAiSuggestions } = useResume();
  const [editMode, setEditMode] = useState<string | null>(null);
  const [showForm, setShowForm] = useState(false);
  const [showSuggestions, setShowSuggestions] = useState(false);
  const [loadingSuggestions, setLoadingSuggestions] = useState(false);
  const [suggestions, setSuggestions] = useState<string[]>([]);
  
  const emptySkill = {
    id: '',
    name: '',
    level: 'Intermediate'
  };
  
  const [formData, setFormData] = useState(emptySkill);

  const skillLevels = ['Beginner', 'Intermediate', 'Advanced', 'Expert'];

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    
    if (editMode) {
      updateSkill(editMode, formData);
    } else {
      addSkill(formData);
    }
    
    setFormData(emptySkill);
    setEditMode(null);
    setShowForm(false);
  };

  const handleEdit = (id: string) => {
    const skillToEdit = resume.skills.find(skill => skill.id === id);
    if (skillToEdit) {
      setFormData(skillToEdit);
      setEditMode(id);
      setShowForm(true);
    }
  };

  const handleDelete = (id: string) => {
    removeSkill(id);
  };

  const handleCancel = () => {
    setFormData(emptySkill);
    setEditMode(null);
    setShowForm(false);
  };

  const handleGetSuggestions = async () => {
    setLoadingSuggestions(true);
    setShowSuggestions(true);
    
    try {
      // Build a context based on experience and education
      const experienceContext = resume.experience.map(exp => 
        `${exp.position} at ${exp.company}`
      ).join(', ');
      
      const educationContext = resume.education.map(edu => 
        `${edu.degree} in ${edu.field} from ${edu.institution}`
      ).join(', ');
      
      const context = `Experience: ${experienceContext || 'N/A'}
        Education: ${educationContext || 'N/A'}`;
      
      const result = await getAiSuggestions('skills', context);
      setSuggestions(result);
    } catch (error) {
      console.error('Error getting suggestions:', error);
    } finally {
      setLoadingSuggestions(false);
    }
  };

  const applySuggestion = (suggestion: string) => {
    // Parse the skills from the suggestion
    // This assumes the suggestion is a comma-separated list of skills
    const skillNames = suggestion.split(',').map(s => s.trim());
    
    // Add each skill to the resume
    skillNames.forEach(name => {
      if (name && !resume.skills.some(s => s.name.toLowerCase() === name.toLowerCase())) {
        addSkill({ id: '', name, level: 'Intermediate' });
      }
    });
    
    setShowSuggestions(false);
  };

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h3 className="text-xl font-semibold text-gray-800">Skills</h3>
        <div className="flex gap-2">
          <button
            type="button"
            onClick={handleGetSuggestions}
            className="flex items-center text-sm px-3 py-1.5 bg-indigo-100 text-indigo-700 rounded-md hover:bg-indigo-200 transition-colors"
          >
            <Sparkles className="h-4 w-4 mr-1" />
            Suggest Skills
          </button>
          {!showForm && (
            <button
              type="button"
              onClick={() => setShowForm(true)}
              className="flex items-center text-sm px-3 py-1.5 bg-blue-100 text-blue-700 rounded-md hover:bg-blue-200 transition-colors"
            >
              <Plus className="h-4 w-4 mr-1" />
              Add Skill
            </button>
          )}
        </div>
      </div>

      {/* Form for adding/editing */}
      {showForm && (
        <form onSubmit={handleSubmit} className="bg-gray-50 p-4 rounded-md mb-4">
          <h4 className="text-lg font-medium text-gray-800 mb-4">
            {editMode ? 'Edit Skill' : 'Add Skill'}
          </h4>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
            <div>
              <label htmlFor="name" className="block text-sm font-medium text-gray-700 mb-1">
                Skill *
              </label>
              <input
                type="text"
                id="name"
                name="name"
                value={formData.name}
                onChange={handleChange}
                required
                className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
                placeholder="Programming language, software, soft skill, etc."
              />
            </div>
            
            <div>
              <label htmlFor="level" className="block text-sm font-medium text-gray-700 mb-1">
                Proficiency Level
              </label>
              <select
                id="level"
                name="level"
                value={formData.level}
                onChange={handleChange}
                className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
              >
                {skillLevels.map(level => (
                  <option key={level} value={level}>{level}</option>
                ))}
              </select>
            </div>
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

      {/* List of skills */}
      {resume.skills.length === 0 ? (
        <p className="text-gray-500 italic">No skills added yet.</p>
      ) : (
        <div className="flex flex-wrap gap-2">
          {resume.skills.map((skill) => (
            <div
              key={skill.id}
              className="bg-white border border-gray-200 rounded-full px-4 py-2 flex items-center gap-2 hover:shadow-sm transition-shadow"
            >
              <span className="text-gray-800">{skill.name}</span>
              {skill.level && (
                <span className="text-xs bg-gray-100 text-gray-600 px-2 py-1 rounded-full">
                  {skill.level}
                </span>
              )}
              <div className="flex gap-1">
                <button
                  onClick={() => handleEdit(skill.id)}
                  className="text-blue-600 hover:text-blue-800"
                  title="Edit"
                >
                  <Edit className="h-4 w-4" />
                </button>
                <button
                  onClick={() => handleDelete(skill.id)}
                  className="text-red-600 hover:text-red-800"
                  title="Delete"
                >
                  <Trash className="h-4 w-4" />
                </button>
              </div>
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

export default SkillsForm;
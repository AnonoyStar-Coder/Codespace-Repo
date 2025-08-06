import { useState } from 'react';
import { useResume } from '../../context/ResumeContext';
import { Plus, Edit, Trash } from 'lucide-react';

const ProjectsForm = () => {
  const { resume, addProject, updateProject, removeProject } = useResume();
  const [editMode, setEditMode] = useState<string | null>(null);
  const [showForm, setShowForm] = useState(false);
  
  const emptyProject = {
    id: '',
    name: '',
    description: '',
    url: '',
    technologies: ''
  };
  
  const [formData, setFormData] = useState(emptyProject);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    
    if (editMode) {
      updateProject(editMode, formData);
    } else {
      addProject(formData);
    }
    
    setFormData(emptyProject);
    setEditMode(null);
    setShowForm(false);
  };

  const handleEdit = (id: string) => {
    const projectToEdit = resume.projects.find(project => project.id === id);
    if (projectToEdit) {
      setFormData(projectToEdit);
      setEditMode(id);
      setShowForm(true);
    }
  };

  const handleDelete = (id: string) => {
    if (window.confirm('Are you sure you want to delete this project?')) {
      removeProject(id);
    }
  };

  const handleCancel = () => {
    setFormData(emptyProject);
    setEditMode(null);
    setShowForm(false);
  };

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h3 className="text-xl font-semibold text-gray-800">Projects</h3>
        {!showForm && (
          <button
            type="button"
            onClick={() => setShowForm(true)}
            className="flex items-center text-sm px-3 py-1.5 bg-blue-100 text-blue-700 rounded-md hover:bg-blue-200 transition-colors"
          >
            <Plus className="h-4 w-4 mr-1" />
            Add Project
          </button>
        )}
      </div>

      {/* Form for adding/editing */}
      {showForm && (
        <form onSubmit={handleSubmit} className="bg-gray-50 p-4 rounded-md mb-4">
          <h4 className="text-lg font-medium text-gray-800 mb-4">
            {editMode ? 'Edit Project' : 'Add Project'}
          </h4>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
            <div className="md:col-span-2">
              <label htmlFor="name" className="block text-sm font-medium text-gray-700 mb-1">
                Project Name *
              </label>
              <input
                type="text"
                id="name"
                name="name"
                value={formData.name}
                onChange={handleChange}
                required
                className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
              />
            </div>
            
            <div className="md:col-span-2">
              <label htmlFor="technologies" className="block text-sm font-medium text-gray-700 mb-1">
                Technologies/Tools Used *
              </label>
              <input
                type="text"
                id="technologies"
                name="technologies"
                value={formData.technologies}
                onChange={handleChange}
                required
                className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
                placeholder="React, Node.js, Python, etc."
              />
            </div>
            
            <div className="md:col-span-2">
              <label htmlFor="url" className="block text-sm font-medium text-gray-700 mb-1">
                Project URL
              </label>
              <input
                type="url"
                id="url"
                name="url"
                value={formData.url}
                onChange={handleChange}
                className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
                placeholder="https://github.com/yourusername/project"
              />
            </div>
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
              placeholder="Describe the project, your role, and its impact"
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

      {/* List of projects */}
      {resume.projects.length === 0 ? (
        <p className="text-gray-500 italic">No projects added yet.</p>
      ) : (
        <div className="space-y-4">
          {resume.projects.map((project) => (
            <div key={project.id} className="bg-white border border-gray-200 rounded-md p-4 hover:shadow-sm transition-shadow">
              <div className="flex justify-between">
                <div>
                  <h4 className="text-lg font-medium text-gray-900">{project.name}</h4>
                  <p className="text-sm text-gray-500">{project.technologies}</p>
                  {project.url && (
                    <a
                      href={project.url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="text-sm text-blue-600 hover:text-blue-800 hover:underline"
                    >
                      Project Link
                    </a>
                  )}
                </div>
                <div className="flex space-x-2">
                  <button
                    onClick={() => handleEdit(project.id)}
                    className="text-blue-600 hover:text-blue-800"
                    title="Edit"
                  >
                    <Edit className="h-5 w-5" />
                  </button>
                  <button
                    onClick={() => handleDelete(project.id)}
                    className="text-red-600 hover:text-red-800"
                    title="Delete"
                  >
                    <Trash className="h-5 w-5" />
                  </button>
                </div>
              </div>
              <p className="mt-2 text-gray-700">{project.description}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default ProjectsForm;
import { createContext, useState, useEffect, useContext, ReactNode } from 'react';
import axios from 'axios';

export interface PersonalInfo {
  name: string;
  email: string;
  phone: string;
  location: string;
  website?: string;
  summary: string;
  title: string;
  profilePicture?: string | null;
}

export interface Experience {
  id: string;
  company: string;
  position: string;
  location: string;
  startDate: string;
  endDate: string;
  current: boolean;
  description: string;
  achievements: string[];
  technologies: string[];
}

export interface Education {
  id: string;
  institution: string;
  degree: string;
  field: string;
  startDate: string;
  endDate: string;
  current: boolean;
  description: string;
  gpa?: string;
  honors?: string[];
  relevantCourses?: string[];
}

export interface Skill {
  id: string;
  name: string;
  level?: string;
  category?: string;
  yearsOfExperience?: number;
}

export interface Project {
  id: string;
  name: string;
  description: string;
  url?: string;
  technologies: string[];
  role?: string;
  teamSize?: number;
  duration?: string;
  impact?: string[];
}

export interface Resume {
  personal: PersonalInfo;
  experience: Experience[];
  education: Education[];
  skills: Skill[];
  projects: Project[];
  template: string;
  created_at?: string;
  updated_at?: string;
}

interface ResumeContextType {
  resume: Resume;
  loading: boolean;
  saving: boolean;
  updatePersonal: (data: PersonalInfo) => void;
  addExperience: (data: Experience) => void;
  updateExperience: (id: string, data: Experience) => void;
  removeExperience: (id: string) => void;
  addEducation: (data: Education) => void;
  updateEducation: (id: string, data: Education) => void;
  removeEducation: (id: string) => void;
  addSkill: (data: Skill) => void;
  updateSkill: (id: string, data: Skill) => void;
  removeSkill: (id: string) => void;
  addProject: (data: Project) => void;
  updateProject: (id: string, data: Project) => void;
  removeProject: (id: string) => void;
  changeTemplate: (template: string) => void;
  saveResume: () => Promise<void>;
  getAiSuggestions: (section: string, context: string) => Promise<string[]>;
  resetResume: () => void;
}

const defaultResume: Resume = {
  personal: {
    name: '',
    email: '',
    phone: '',
    location: '',
    website: '',
    summary: '',
    title: '',
    profilePicture: null
  },
  experience: [],
  education: [],
  skills: [],
  projects: [],
  template: 'modern'
};

const ResumeContext = createContext<ResumeContextType | undefined>(undefined);

export const ResumeProvider = ({ children }: { children: ReactNode }) => {
  const [resume, setResume] = useState<Resume>(defaultResume);
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);

  useEffect(() => {
    const fetchResume = async () => {
      try {
        const response = await axios.get('/api/resume');
        if (response.data) {
          setResume(response.data);
        }
      } catch (error) {
        console.error('Error fetching resume:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchResume();
  }, []);

  const generateId = () => Math.random().toString(36).substr(2, 9);

  const updatePersonal = (data: PersonalInfo) => {
    setResume(prev => ({ ...prev, personal: data }));
  };

  const addExperience = (data: Experience) => {
    const newExp = { ...data, id: generateId() };
    setResume(prev => ({
      ...prev,
      experience: [...prev.experience, newExp]
    }));
  };

  const updateExperience = (id: string, data: Experience) => {
    setResume(prev => ({
      ...prev,
      experience: prev.experience.map(exp => 
        exp.id === id ? { ...data, id } : exp
      )
    }));
  };

  const removeExperience = (id: string) => {
    setResume(prev => ({
      ...prev,
      experience: prev.experience.filter(exp => exp.id !== id)
    }));
  };

  const addEducation = (data: Education) => {
    const newEdu = { ...data, id: generateId() };
    setResume(prev => ({
      ...prev,
      education: [...prev.education, newEdu]
    }));
  };

  const updateEducation = (id: string, data: Education) => {
    setResume(prev => ({
      ...prev,
      education: prev.education.map(edu => 
        edu.id === id ? { ...data, id } : edu
      )
    }));
  };

  const removeEducation = (id: string) => {
    setResume(prev => ({
      ...prev,
      education: prev.education.filter(edu => edu.id !== id)
    }));
  };

  const addSkill = (data: Skill) => {
    const newSkill = { ...data, id: generateId() };
    setResume(prev => ({
      ...prev,
      skills: [...prev.skills, newSkill]
    }));
  };

  const updateSkill = (id: string, data: Skill) => {
    setResume(prev => ({
      ...prev,
      skills: prev.skills.map(skill => 
        skill.id === id ? { ...data, id } : skill
      )
    }));
  };

  const removeSkill = (id: string) => {
    setResume(prev => ({
      ...prev,
      skills: prev.skills.filter(skill => skill.id !== id)
    }));
  };

  const addProject = (data: Project) => {
    const newProject = { ...data, id: generateId() };
    setResume(prev => ({
      ...prev,
      projects: [...prev.projects, newProject]
    }));
  };

  const updateProject = (id: string, data: Project) => {
    setResume(prev => ({
      ...prev,
      projects: prev.projects.map(project => 
        project.id === id ? { ...data, id } : project
      )
    }));
  };

  const removeProject = (id: string) => {
    setResume(prev => ({
      ...prev,
      projects: prev.projects.filter(project => project.id !== id)
    }));
  };

  const changeTemplate = (template: string) => {
    setResume(prev => ({ ...prev, template }));
  };

  const saveResume = async () => {
    setSaving(true);
    try {
      await axios.post('/api/resume', resume);
    } catch (error) {
      console.error('Error saving resume:', error);
    } finally {
      setSaving(false);
    }
  };

  const getAiSuggestions = async (section: string, context: string) => {
    try {
      const response = await axios.post('/api/ai/suggest', { section, context });
      return response.data.suggestions;
    } catch (error) {
      console.error('Error getting AI suggestions:', error);
      return [];
    }
  };

  const resetResume = () => {
    setResume(defaultResume);
  };

  return (
    <ResumeContext.Provider
      value={{
        resume,
        loading,
        saving,
        updatePersonal,
        addExperience,
        updateExperience,
        removeExperience,
        addEducation,
        updateEducation,
        removeEducation,
        addSkill,
        updateSkill,
        removeSkill,
        addProject,
        updateProject,
        removeProject,
        changeTemplate,
        saveResume,
        getAiSuggestions,
        resetResume
      }}
    >
      {children}
    </ResumeContext.Provider>
  );
};

export const useResume = () => {
  const context = useContext(ResumeContext);
  if (context === undefined) {
    throw new Error('useResume must be used within a ResumeProvider');
  }
  return context;
};
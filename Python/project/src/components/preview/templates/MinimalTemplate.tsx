import { Resume } from '../../../context/ResumeContext';

interface TemplateProps {
  resume: Resume;
}

const MinimalTemplate = ({ resume }: TemplateProps) => {
  const formatDate = (dateString: string) => {
    if (!dateString) return '';
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', { year: 'numeric', month: 'short' });
  };

  return (
    <div className="bg-white p-10 shadow-none min-h-[1000px] max-w-4xl mx-auto text-gray-800 font-light">
      {/* Header */}
      <header className="mb-8 text-center">
        <h1 className="text-3xl font-normal text-gray-900 mb-2">{resume.personal.name || 'Your Name'}</h1>
        
        <div className="text-sm text-gray-600 space-x-2">
          {resume.personal.email && <span>{resume.personal.email}</span>}
          {resume.personal.email && resume.personal.phone && <span>•</span>}
          {resume.personal.phone && <span>{resume.personal.phone}</span>}
          {(resume.personal.email || resume.personal.phone) && resume.personal.location && <span>•</span>}
          {resume.personal.location && <span>{resume.personal.location}</span>}
          {(resume.personal.email || resume.personal.phone || resume.personal.location) && resume.personal.website && <span>•</span>}
          {resume.personal.website && <span>{resume.personal.website}</span>}
        </div>
      </header>

      {/* Summary */}
      {resume.personal.summary && (
        <section className="mb-6">
          <p className="text-center text-gray-700 max-w-3xl mx-auto">{resume.personal.summary}</p>
        </section>
      )}

      <hr className="border-gray-200 my-6" />

      {/* Experience */}
      {resume.experience.length > 0 && (
        <section className="mb-6">
          <h2 className="text-base font-normal text-gray-900 uppercase tracking-widest mb-4 text-center">Experience</h2>
          
          <div className="space-y-5">
            {resume.experience.map((exp) => (
              <div key={exp.id} className="flex flex-col md:flex-row">
                <div className="md:w-1/4 mb-2 md:mb-0 md:pr-6 md:text-right">
                  <p className="text-sm text-gray-500">
                    {formatDate(exp.startDate)} — {exp.current ? 'Present' : formatDate(exp.endDate)}
                  </p>
                  <p className="font-medium text-gray-900">{exp.company}</p>
                  {exp.location && <p className="text-sm text-gray-600">{exp.location}</p>}
                </div>
                <div className="md:w-3/4">
                  <h3 className="font-medium text-gray-900 mb-1">{exp.position}</h3>
                  <p className="text-gray-700 whitespace-pre-line">{exp.description}</p>
                </div>
              </div>
            ))}
          </div>
        </section>
      )}

      {/* Education */}
      {resume.education.length > 0 && (
        <section className="mb-6">
          <h2 className="text-base font-normal text-gray-900 uppercase tracking-widest mb-4 text-center">Education</h2>
          
          <div className="space-y-5">
            {resume.education.map((edu) => (
              <div key={edu.id} className="flex flex-col md:flex-row">
                <div className="md:w-1/4 mb-2 md:mb-0 md:pr-6 md:text-right">
                  <p className="text-sm text-gray-500">
                    {formatDate(edu.startDate)} — {edu.current ? 'Present' : formatDate(edu.endDate)}
                  </p>
                  <p className="font-medium text-gray-900">{edu.institution}</p>
                </div>
                <div className="md:w-3/4">
                  <h3 className="font-medium text-gray-900 mb-1">{edu.degree} in {edu.field}</h3>
                  {edu.description && <p className="text-gray-700">{edu.description}</p>}
                </div>
              </div>
            ))}
          </div>
        </section>
      )}

      {/* Skills */}
      {resume.skills.length > 0 && (
        <section className="mb-6">
          <h2 className="text-base font-normal text-gray-900 uppercase tracking-widest mb-4 text-center">Skills</h2>
          
          <div className="text-center mx-auto max-w-3xl">
            {resume.skills.map((skill, index) => (
              <span key={skill.id} className="inline-block">
                {skill.name}
                {index < resume.skills.length - 1 ? <span className="mx-2 text-gray-400">•</span> : ''}
              </span>
            ))}
          </div>
        </section>
      )}

      {/* Projects */}
      {resume.projects.length > 0 && (
        <section className="mb-6">
          <h2 className="text-base font-normal text-gray-900 uppercase tracking-widest mb-4 text-center">Projects</h2>
          
          <div className="space-y-5">
            {resume.projects.map((project) => (
              <div key={project.id} className="flex flex-col md:flex-row">
                <div className="md:w-1/4 mb-2 md:mb-0 md:pr-6 md:text-right">
                  <p className="font-medium text-gray-900">{project.name}</p>
                  <p className="text-sm text-gray-600">{project.technologies}</p>
                  {project.url && (
                    <a 
                      href={project.url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="text-sm text-gray-500 hover:text-gray-700"
                    >
                      View Project
                    </a>
                  )}
                </div>
                <div className="md:w-3/4">
                  <p className="text-gray-700">{project.description}</p>
                </div>
              </div>
            ))}
          </div>
        </section>
      )}
    </div>
  );
};

export default MinimalTemplate;
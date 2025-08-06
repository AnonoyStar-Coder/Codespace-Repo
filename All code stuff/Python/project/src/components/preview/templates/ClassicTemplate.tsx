import { Resume } from '../../../context/ResumeContext';

interface TemplateProps {
  resume: Resume;
}

const ClassicTemplate = ({ resume }: TemplateProps) => {
  const formatDate = (dateString: string) => {
    if (!dateString) return '';
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', { year: 'numeric', month: 'short' });
  };

  return (
    <div className="bg-white p-8 shadow-none min-h-[1000px] max-w-4xl mx-auto text-gray-800 relative">
      {/* Header */}
      <header className="text-center border-b border-gray-300 pb-4 mb-6">
        <h1 className="text-3xl font-bold text-gray-900 uppercase tracking-wider">{resume.personal.name || 'Your Name'}</h1>
        
        <div className="mt-2 flex flex-wrap justify-center text-sm">
          {resume.personal.email && (
            <div className="mx-2 mb-1">
              <span>{resume.personal.email}</span>
            </div>
          )}
          
          {resume.personal.phone && (
            <div className="mx-2 mb-1">
              <span>{resume.personal.phone}</span>
            </div>
          )}
          
          {resume.personal.location && (
            <div className="mx-2 mb-1">
              <span>{resume.personal.location}</span>
            </div>
          )}
          
          {resume.personal.website && (
            <div className="mx-2 mb-1">
              <span>{resume.personal.website}</span>
            </div>
          )}
        </div>
      </header>

      {/* Summary */}
      {resume.personal.summary && (
        <section className="mb-6">
          <h2 className="text-lg font-bold text-gray-900 uppercase tracking-wider border-b border-gray-300 pb-1 mb-3">Objective</h2>
          <p className="text-gray-700">{resume.personal.summary}</p>
        </section>
      )}

      {/* Experience */}
      {resume.experience.length > 0 && (
        <section className="mb-6">
          <h2 className="text-lg font-bold text-gray-900 uppercase tracking-wider border-b border-gray-300 pb-1 mb-3">Professional Experience</h2>
          
          <div className="space-y-4">
            {resume.experience.map((exp) => (
              <div key={exp.id} className="ml-0">
                <div className="flex justify-between items-start">
                  <div>
                    <h3 className="font-bold text-gray-800">{exp.position}</h3>
                    <p className="text-gray-700">{exp.company}{exp.location ? `, ${exp.location}` : ''}</p>
                  </div>
                  <p className="text-sm text-gray-600 whitespace-nowrap">
                    {formatDate(exp.startDate)} - {exp.current ? 'Present' : formatDate(exp.endDate)}
                  </p>
                </div>
                <p className="mt-2 text-gray-700 whitespace-pre-line">{exp.description}</p>
              </div>
            ))}
          </div>
        </section>
      )}

      {/* Education */}
      {resume.education.length > 0 && (
        <section className="mb-6">
          <h2 className="text-lg font-bold text-gray-900 uppercase tracking-wider border-b border-gray-300 pb-1 mb-3">Education</h2>
          
          <div className="space-y-4">
            {resume.education.map((edu) => (
              <div key={edu.id} className="ml-0">
                <div className="flex justify-between items-start">
                  <div>
                    <h3 className="font-bold text-gray-800">{edu.degree} in {edu.field}</h3>
                    <p className="text-gray-700">{edu.institution}</p>
                  </div>
                  <p className="text-sm text-gray-600 whitespace-nowrap">
                    {formatDate(edu.startDate)} - {edu.current ? 'Present' : formatDate(edu.endDate)}
                  </p>
                </div>
                {edu.description && <p className="mt-2 text-gray-700">{edu.description}</p>}
              </div>
            ))}
          </div>
        </section>
      )}

      {/* Skills */}
      {resume.skills.length > 0 && (
        <section className="mb-6">
          <h2 className="text-lg font-bold text-gray-900 uppercase tracking-wider border-b border-gray-300 pb-1 mb-3">Skills</h2>
          
          <ul className="list-disc pl-5 text-gray-700">
            {resume.skills.map((skill) => (
              <li key={skill.id}>
                {skill.name}{skill.level ? ` - ${skill.level}` : ''}
              </li>
            ))}
          </ul>
        </section>
      )}

      {/* Projects */}
      {resume.projects.length > 0 && (
        <section className="mb-6">
          <h2 className="text-lg font-bold text-gray-900 uppercase tracking-wider border-b border-gray-300 pb-1 mb-3">Projects</h2>
          
          <div className="space-y-4">
            {resume.projects.map((project) => (
              <div key={project.id} className="ml-0">
                <div className="flex justify-between items-start">
                  <h3 className="font-bold text-gray-800">
                    {project.name}
                    {project.url && (
                      <a 
                        href={project.url} 
                        target="_blank" 
                        rel="noopener noreferrer" 
                        className="ml-2 text-sm text-gray-600 hover:underline"
                      >
                        (Link)
                      </a>
                    )}
                  </h3>
                </div>
                <p className="text-sm text-gray-600">{project.technologies}</p>
                <p className="mt-1 text-gray-700">{project.description}</p>
              </div>
            ))}
          </div>
        </section>
      )}
    </div>
  );
};

export default ClassicTemplate;
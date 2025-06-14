import { Resume } from '../../../context/ResumeContext';

interface TemplateProps {
  resume: Resume;
}

const CreativeTemplate = ({ resume }: TemplateProps) => {
  const formatDate = (dateString: string) => {
    if (!dateString) return '';
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', { year: 'numeric', month: 'short' });
  };

  return (
    <div className="bg-white shadow-none min-h-[1000px] max-w-4xl mx-auto text-gray-800 relative">
      {/* Header with background color */}
      <header className="bg-purple-700 text-white p-8">
        <h1 className="text-4xl font-bold">{resume.personal.name || 'Your Name'}</h1>
        
        {resume.personal.summary && (
          <p className="mt-3 text-purple-100 font-light leading-relaxed">
            {resume.personal.summary}
          </p>
        )}
        
        <div className="mt-4 flex flex-wrap text-sm">
          {resume.personal.email && (
            <div className="mr-4 mb-2 flex items-center">
              <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 mr-1" viewBox="0 0 20 20" fill="currentColor">
                <path d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z" />
                <path d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z" />
              </svg>
              <span>{resume.personal.email}</span>
            </div>
          )}
          
          {resume.personal.phone && (
            <div className="mr-4 mb-2 flex items-center">
              <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 mr-1" viewBox="0 0 20 20" fill="currentColor">
                <path d="M2 3a1 1 0 011-1h2.153a1 1 0 01.986.836l.74 4.435a1 1 0 01-.54 1.06l-1.548.773a11.037 11.037 0 006.105 6.105l.774-1.548a1 1 0 011.059-.54l4.435.74a1 1 0 01.836.986V17a1 1 0 01-1 1h-2C7.82 18 2 12.18 2 5V3z" />
              </svg>
              <span>{resume.personal.phone}</span>
            </div>
          )}
          
          {resume.personal.location && (
            <div className="mr-4 mb-2 flex items-center">
              <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 mr-1" viewBox="0 0 20 20" fill="currentColor">
                <path fillRule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clipRule="evenodd" />
              </svg>
              <span>{resume.personal.location}</span>
            </div>
          )}
          
          {resume.personal.website && (
            <div className="mb-2 flex items-center">
              <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 mr-1" viewBox="0 0 20 20" fill="currentColor">
                <path fillRule="evenodd" d="M12.586 4.586a2 2 0 112.828 2.828l-3 3a2 2 0 01-2.828 0 1 1 0 00-1.414 1.414 4 4 0 005.656 0l3-3a4 4 0 00-5.656-5.656l-1.5 1.5a1 1 0 101.414 1.414l1.5-1.5zm-5 5a2 2 0 012.828 0 1 1 0 101.414-1.414 4 4 0 00-5.656 0l-3 3a4 4 0 105.656 5.656l1.5-1.5a1 1 0 10-1.414-1.414l-1.5 1.5a2 2 0 11-2.828-2.828l3-3z" clipRule="evenodd" />
              </svg>
              <span>{resume.personal.website}</span>
            </div>
          )}
        </div>
      </header>

      <div className="grid grid-cols-3 gap-6 p-8">
        {/* Left column */}
        <div className="col-span-1 space-y-6">
          {/* Skills */}
          {resume.skills.length > 0 && (
            <section>
              <h2 className="text-xl font-bold text-purple-700 mb-3 border-b-2 border-purple-200 pb-1">Skills</h2>
              
              <div className="space-y-2">
                {resume.skills.map((skill) => (
                  <div key={skill.id} className="flex flex-col">
                    <div className="flex justify-between items-center">
                      <span className="font-medium text-gray-800">{skill.name}</span>
                      {skill.level && <span className="text-xs text-gray-500">{skill.level}</span>}
                    </div>
                    {skill.level && (
                      <div className="w-full bg-gray-200 rounded-full h-1.5 mt-1">
                        <div 
                          className="bg-purple-600 h-1.5 rounded-full" 
                          style={{ 
                            width: skill.level === 'Beginner' ? '25%' :
                                   skill.level === 'Intermediate' ? '50%' :
                                   skill.level === 'Advanced' ? '75%' : '100%'
                          }}
                        ></div>
                      </div>
                    )}
                  </div>
                ))}
              </div>
            </section>
          )}

          {/* Education */}
          {resume.education.length > 0 && (
            <section>
              <h2 className="text-xl font-bold text-purple-700 mb-3 border-b-2 border-purple-200 pb-1">Education</h2>
              
              <div className="space-y-4">
                {resume.education.map((edu) => (
                  <div key={edu.id}>
                    <h3 className="font-semibold text-gray-800">{edu.degree} in {edu.field}</h3>
                    <p className="text-gray-700">{edu.institution}</p>
                    <p className="text-sm text-gray-500">
                      {formatDate(edu.startDate)} - {edu.current ? 'Present' : formatDate(edu.endDate)}
                    </p>
                    {edu.description && <p className="mt-1 text-sm text-gray-600">{edu.description}</p>}
                  </div>
                ))}
              </div>
            </section>
          )}
        </div>

        {/* Right column */}
        <div className="col-span-2 space-y-6">
          {/* Experience */}
          {resume.experience.length > 0 && (
            <section>
              <h2 className="text-xl font-bold text-purple-700 mb-4 border-b-2 border-purple-200 pb-1">Work Experience</h2>
              
              <div className="space-y-5">
                {resume.experience.map((exp) => (
                  <div key={exp.id} className="relative pl-6 before:content-[''] before:absolute before:left-0 before:top-1.5 before:w-3 before:h-3 before:bg-purple-600 before:rounded-full before:z-10 after:content-[''] after:absolute after:left-1.5 after:top-1.5 after:h-full after:w-0.5 after:bg-purple-200 after:-z-10 last:after:hidden">
                    <div className="mb-1">
                      <h3 className="font-bold text-gray-900">{exp.position}</h3>
                      <p className="text-purple-700">{exp.company}{exp.location ? `, ${exp.location}` : ''}</p>
                      <p className="text-sm text-gray-500 mb-2">
                        {formatDate(exp.startDate)} - {exp.current ? 'Present' : formatDate(exp.endDate)}
                      </p>
                    </div>
                    <p className="text-gray-700 whitespace-pre-line">{exp.description}</p>
                  </div>
                ))}
              </div>
            </section>
          )}

          {/* Projects */}
          {resume.projects.length > 0 && (
            <section>
              <h2 className="text-xl font-bold text-purple-700 mb-4 border-b-2 border-purple-200 pb-1">Projects</h2>
              
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                {resume.projects.map((project) => (
                  <div key={project.id} className="border border-purple-100 rounded-lg p-4 hover:shadow-md transition-shadow">
                    <h3 className="font-bold text-gray-900 mb-1">
                      {project.name}
                      {project.url && (
                        <a 
                          href={project.url} 
                          target="_blank" 
                          rel="noopener noreferrer" 
                          className="ml-2 text-xs text-purple-600 hover:underline"
                        >
                          View Project
                        </a>
                      )}
                    </h3>
                    <p className="text-xs text-purple-600 font-medium mb-2">{project.technologies}</p>
                    <p className="text-sm text-gray-700">{project.description}</p>
                  </div>
                ))}
              </div>
            </section>
          )}
        </div>
      </div>
    </div>
  );
};

export default CreativeTemplate;
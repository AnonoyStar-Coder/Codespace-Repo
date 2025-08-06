import { useResume } from '../../context/ResumeContext';
import ModernTemplate from './templates/ModernTemplate';
import ClassicTemplate from './templates/ClassicTemplate';
import CreativeTemplate from './templates/CreativeTemplate';
import MinimalTemplate from './templates/MinimalTemplate';

const ResumePreviewPane = () => {
  const { resume } = useResume();

  const renderTemplate = () => {
    switch (resume.template) {
      case 'modern':
        return <ModernTemplate resume={resume} />;
      case 'classic':
        return <ClassicTemplate resume={resume} />;
      case 'creative':
        return <CreativeTemplate resume={resume} />;
      case 'minimal':
        return <MinimalTemplate resume={resume} />;
      default:
        return <ModernTemplate resume={resume} />;
    }
  };

  return (
    <div className="resume-preview-container">
      {renderTemplate()}
    </div>
  );
};

export default ResumePreviewPane;
import { useEffect, useRef, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useResume } from '../context/ResumeContext';
import { Download, Edit, Share } from 'lucide-react';
import axios from 'axios';
import html2canvas from 'html2canvas';
import jsPDF from 'jspdf';
import ResumePreviewPane from '../components/preview/ResumePreviewPane';

const ResumePreview = () => {
  const { resume, loading } = useResume();
  const resumeRef = useRef<HTMLDivElement>(null);
  const [generating, setGenerating] = useState(false);
  const [shareUrl, setShareUrl] = useState<string | null>(null);
  const [copied, setCopied] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    if (!loading && !resume.personal.name) {
      navigate('/builder');
    }
  }, [loading, resume, navigate]);

  const generatePDF = async () => {
    if (!resumeRef.current) return;

    setGenerating(true);
    
    try {
      const canvas = await html2canvas(resumeRef.current, {
        scale: 2,
        logging: false,
        useCORS: true
      });
      
      const imgData = canvas.toDataURL('image/png');
      const pdf = new jsPDF({
        orientation: 'portrait',
        unit: 'px',
        format: [canvas.width / 2, canvas.height / 2]
      });
      
      pdf.addImage(imgData, 'PNG', 0, 0, canvas.width / 2, canvas.height / 2);
      pdf.save(`${resume.personal.name.replace(/\s+/g, '_')}_Resume.pdf`);
    } catch (error) {
      console.error('Error generating PDF:', error);
      // Fallback to server-side PDF generation
      try {
        const response = await axios.get('/export/pdf', { responseType: 'blob' });
        const url = window.URL.createObjectURL(new Blob([response.data]));
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute('download', `${resume.personal.name.replace(/\s+/g, '_')}_Resume.pdf`);
        document.body.appendChild(link);
        link.click();
        link.remove();
      } catch (serverError) {
        console.error('Server-side PDF generation failed:', serverError);
        alert('Failed to generate PDF. Please try again later.');
      }
    } finally {
      setGenerating(false);
    }
  };

  const handleShare = () => {
    // In a real app, this would generate a shareable link
    // For this demo, we'll just simulate it
    const demoShareUrl = `${window.location.origin}/shared/${Math.random().toString(36).substring(2, 10)}`;
    setShareUrl(demoShareUrl);
  };

  const copyShareUrl = () => {
    if (shareUrl) {
      navigator.clipboard.writeText(shareUrl);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    }
  };

  if (loading) {
    return (
      <div className="h-screen flex items-center justify-center pt-16">
        <div className="loading-spinner"></div>
      </div>
    );
  }

  return (
    <div className="container mx-auto pt-20 pb-8 px-4">
      <div className="bg-white rounded-lg shadow-sm p-6 mb-6">
        <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4 mb-6">
          <h1 className="text-2xl font-bold text-gray-800">Resume Preview</h1>
          <div className="flex flex-wrap gap-3">
            <button
              onClick={() => navigate('/builder')}
              className="flex items-center gap-2 px-4 py-2 bg-gray-200 text-gray-800 rounded-md hover:bg-gray-300 transition-colors"
            >
              <Edit className="w-4 h-4" />
              Edit Resume
            </button>
            <button
              onClick={handleShare}
              className="flex items-center gap-2 px-4 py-2 bg-indigo-600 text-white rounded-md hover:bg-indigo-700 transition-colors"
            >
              <Share className="w-4 h-4" />
              Share
            </button>
            <button
              onClick={generatePDF}
              disabled={generating}
              className="flex items-center gap-2 px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition-colors disabled:opacity-70"
            >
              <Download className="w-4 h-4" />
              {generating ? 'Generating...' : 'Download PDF'}
            </button>
          </div>
        </div>

        {shareUrl && (
          <div className="mb-6 p-4 bg-gray-50 rounded-md">
            <p className="mb-2 text-gray-700">Share this resume with others:</p>
            <div className="flex gap-2">
              <input
                type="text"
                readOnly
                value={shareUrl}
                className="flex-grow px-3 py-2 border border-gray-300 rounded-md text-sm"
              />
              <button
                onClick={copyShareUrl}
                className="px-3 py-2 bg-gray-200 hover:bg-gray-300 rounded-md text-sm font-medium transition-colors"
              >
                {copied ? 'Copied!' : 'Copy'}
              </button>
            </div>
          </div>
        )}

        <div className="mx-auto max-w-4xl bg-white shadow-md rounded-md overflow-hidden" ref={resumeRef}>
          <ResumePreviewPane />
        </div>
      </div>
    </div>
  );
};

export default ResumePreview;
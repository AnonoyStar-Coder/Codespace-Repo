from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import os
import json
from datetime import datetime
import secrets
from werkzeug.utils import secure_filename
import openai

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload

# Set up OpenAI API key - in production, use environment variables
# openai.api_key = os.getenv("OPENAI_API_KEY")
# Mock API key for demo purposes
openai.api_key = "your-api-key-here"

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# In-memory storage for demo purposes - in production use a database
RESUMES = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/builder')
def builder():
    # Generate a unique ID for this resume session if not exists
    if 'resume_id' not in session:
        session['resume_id'] = secrets.token_hex(8)
        RESUMES[session['resume_id']] = {
            'personal': {
                'name': '',
                'email': '',
                'phone': '',
                'location': '',
                'website': '',
                'summary': '',
                'title': '',
                'profilePicture': None
            },
            'experience': [],
            'education': [],
            'skills': [],
            'projects': [],
            'template': 'modern',
            'created_at': datetime.now().isoformat()
        }
    
    return render_template('builder.html', 
                          resume_data=RESUMES.get(session['resume_id'], {}))

@app.route('/api/resume', methods=['GET', 'POST'])
def handle_resume():
    resume_id = session.get('resume_id')
    if not resume_id:
        return jsonify({'error': 'No active session'}), 400
    
    if request.method == 'GET':
        return jsonify(RESUMES.get(resume_id, {}))
    
    if request.method == 'POST':
        data = request.get_json()
        RESUMES[resume_id] = data
        RESUMES[resume_id]['updated_at'] = datetime.now().isoformat()
        return jsonify({'status': 'success', 'resume_id': resume_id})

@app.route('/api/ai/suggest', methods=['POST'])
def ai_suggest():
    data = request.get_json()
    section = data.get('section')
    context = data.get('context', '')
    
    # For demo purposes - in production, use actual OpenAI API call
    suggestions = generate_ai_suggestions(section, context)
    
    return jsonify({'suggestions': suggestions})

@app.route('/preview')
def preview():
    resume_id = session.get('resume_id')
    if not resume_id or resume_id not in RESUMES:
        return redirect(url_for('builder'))
    
    return render_template('preview.html', 
                          resume_data=RESUMES.get(resume_id, {}))

@app.route('/export/pdf')
def export_pdf():
    # This would generate a PDF in production
    # For demo, we just return a success message
    return jsonify({'status': 'success', 'message': 'PDF would be generated here'})

def generate_ai_suggestions(section, context):
    """
    Generate AI suggestions for different resume sections
    In production, this would call the OpenAI API
    """
    suggestions = []
    
    # Mock suggestions based on section
    if section == 'experience':
        suggestions = [
            "Led cross-functional team of 8 engineers in developing and launching a new e-commerce platform, resulting in 45% increase in online sales",
            "Implemented automated testing framework reducing QA time by 60% and improving code coverage to 95%",
            "Architected and deployed microservices infrastructure supporting 1M+ daily active users with 99.99% uptime"
        ]
    elif section == 'skills':
        suggestions = [
            "Full Stack Development (React, Node.js, Python)",
            "Cloud Architecture (AWS, Azure, GCP)",
            "Machine Learning & AI (TensorFlow, PyTorch, scikit-learn)"
        ]
    elif section == 'summary':
        suggestions = [
            "Results-driven technology leader with 8+ years of experience in building scalable web applications and leading high-performance engineering teams",
            "Innovative software architect specializing in cloud-native solutions with a track record of delivering enterprise-scale projects on time and under budget",
            "Forward-thinking engineering manager combining technical expertise with strong business acumen to drive digital transformation initiatives"
        ]
    
    return suggestions

if __name__ == '__main__':
    app.run(debug=True)
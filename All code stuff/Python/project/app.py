from flask import Flask, request, jsonify, session, redirect, url_for, send_from_directory
import os
import json
from datetime import datetime
import secrets
from werkzeug.utils import secure_filename
import requests

app = Flask(__name__, static_folder='dist', static_url_path='')
app.secret_key = secrets.token_hex(16)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# In-memory storage for demo purposes
RESUMES = {}

# Ollama config
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "mistral"

# Serve built React frontend directly
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/resume', methods=['GET', 'POST'])
def handle_resume():
    resume_id = session.get('resume_id')
    if not resume_id:
        # generate resume_id for new session
        session['resume_id'] = secrets.token_hex(8)
        resume_id = session['resume_id']
        RESUMES[resume_id] = {
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
    resume_id = session.get('resume_id')

    if not resume_id or resume_id not in RESUMES:
        return jsonify({'error': 'No active session data'}), 400

    resume_data = RESUMES[resume_id]

    suggestions = generate_local_ai_suggestions(section, resume_data)
    return jsonify({'suggestions': suggestions})

def generate_local_ai_suggestions(section, resume_data):
    job_title = resume_data.get("personal", {}).get("title", "professional")
    summary = resume_data.get("personal", {}).get("summary", "")
    skills_list = resume_data.get("skills", [])
    skills = ", ".join(skill.get("name", "") if isinstance(skill, dict) else str(skill) for skill in skills_list)

    if section == 'experience':
        prompt = f"""
You are a professional resume assistant. Based on the following user profile, suggest 3 bullet points that can be added to their experience section.

User Information:
- Job Title: {job_title}
- Skills: {skills}
- Summary: {summary}

Generate 3 professional, impactful, ATS-friendly bullet points.
"""
    elif section == 'skills':
        prompt = f"""
You are a resume assistant. Based on the user's current skills, suggest 5 relevant technical and 5 relevant soft skills as a list of names only, with no descriptions or explanations.

Current Skills: {skills}
"""

    elif section == 'summary':
        prompt = f"""
You are a resume assistant. Suggest 3 professional resume summary statements based on the following:

- Job Title: {job_title}
- Skills: {skills}
- Summary: {summary}

Make it sound professional, concise and tailored.
"""
    else:
        return ["Invalid section."]

    try:
        response = requests.post(OLLAMA_URL, json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        })
        response.raise_for_status()
        result = response.json()
        output = result.get("response", "")

        suggestions = [s.strip(" -•") for s in output.split("\n") if s.strip()]
        return suggestions

    except Exception as e:
        return [f"Error generating suggestions: {str(e)}"]

@app.route('/export/pdf')
def export_pdf():
    return jsonify({'status': 'success', 'message': 'PDF would be generated here'})

if __name__ == '__main__':
    app.run(debug=True)


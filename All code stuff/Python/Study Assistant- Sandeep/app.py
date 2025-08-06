import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Helper functions to handle file persistence

# Planner: Save new task
def save_task(task_data):
    with open('tasks.json', 'a') as f:
        json.dump(task_data, f)
        f.write("\n")

# Planner: Load all tasks
def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            tasks = [json.loads(line) for line in f]
    except FileNotFoundError:
        tasks = []
    return tasks

# Notes: Save new note
def save_note(content):
    with open('notes.json', 'a') as f:
        json.dump({'content': content}, f)
        f.write("\n")

# Notes: Load all notes
def load_notes():
    try:
        with open('notes.json', 'r') as f:
            notes = [json.loads(line) for line in f]
    except FileNotFoundError:
        notes = []
    return notes

# Reminders: Save new reminder
def save_reminder(reminder_data):
    with open('reminders.json', 'a') as f:
        json.dump(reminder_data, f)
        f.write("\n")

# Reminders: Load all reminders
def load_reminders():
    try:
        with open('reminders.json', 'r') as f:
            reminders = [json.loads(line) for line in f]
    except FileNotFoundError:
        reminders = []
    return reminders

# Routes

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Login route
@app.route('/login')
def login():
    return render_template('login.html')

# Dashboard route
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Home Page Route
@app.route('/home')
def home():
    return render_template('home.html')

# Resources Page Route
@app.route('/resources')
def resources():
    return render_template('resources.html')

# Notes Route
@app.route('/notes', methods=['GET', 'POST'])
def notes():
    if request.method == 'POST':
        note_content = request.form['note']
        save_note(note_content)
    notes = load_notes()
    return render_template('notes.html', notes=notes)

# Planner Route
@app.route('/planner', methods=['GET', 'POST'])
def planner():
    if request.method == 'POST':
        task_data = {'task': request.form['task'], 'due_date': request.form['due_date']}
        save_task(task_data)
    tasks = load_tasks()
    return render_template('planner.html', tasks=tasks)

# Reminders Route
@app.route('/reminders', methods=['GET', 'POST'])
def reminders():
    if request.method == 'POST':
        reminder_data = {'reminder': request.form['reminder'], 'due_date': request.form['due_date']}
        save_reminder(reminder_data)
    reminders = load_reminders()
    return render_template('reminders.html', reminders=reminders)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)

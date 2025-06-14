#!/bin/bash

# ====================================
# ⚔️ THE GREAT BALLU RESURRECTION ⚔️
# ====================================

echo "🌄 Starting full resurrection..."

# Move to project root
cd "$(dirname "$0")" || exit 1

# === FRONTEND BUILD ===
echo "🧹 Cleaning old node_modules..."
rm -rf node_modules package-lock.json

echo "📦 Installing frontend dependencies..."
npm install

echo "🏗️ Building frontend..."
npm run build

if [ ! -d "dist" ]; then
  echo "❌ Frontend build failed. No dist folder found."
  exit 1
fi

# === PYTHON BACKEND ===
echo "🐍 Checking Python dependencies..."

if [ -f "requirements.txt" ]; then
  python3 -m venv venv
  source venv/bin/activate
  pip install --upgrade pip
  pip install -r requirements.txt
else
  echo "⚠️ No requirements.txt found. Skipping Python deps install."
fi

# === SERVE FLASK APP ===
echo "🚀 Launching Flask server..."

export FLASK_APP=app.py
export FLASK_ENV=development
flask run


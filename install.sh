#!/bin/bash
echo "📦 Installing backend Python packages..."
pip install -r requirements.txt

echo "📦 Installing frontend NPM packages..."
cd frontend
npm install
cd ..

#!/bin/bash
# Quick deployment setup script

echo "🚀 Critical Minerals Tracker - Deployment Setup"
echo "================================================"
echo ""

# Check if git is initialized
if [ ! -d .git ]; then
    echo "📦 Initializing git repository..."
    git init
    echo "✓ Git initialized"
else
    echo "✓ Git already initialized"
fi

# Add all files
echo "📝 Adding files to git..."
git add .
echo "✓ Files added"

# Commit
echo "💾 Creating initial commit..."
git commit -m "Initial commit - Critical Minerals Tracker for ClearPath" || echo "✓ Files already committed"

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Create a GitHub repository at: https://github.com/new"
echo "   - Name it: minerals-tracker"
echo "   - Make it PRIVATE"
echo "   - Don't initialize with README"
echo ""
echo "2. Then run these commands (GitHub will show them to you):"
echo "   git remote add origin https://github.com/YOUR-USERNAME/minerals-tracker.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "3. Deploy to Streamlit Cloud:"
echo "   - Go to: https://share.streamlit.io/"
echo "   - Click 'New app'"
echo "   - Select your repository"
echo "   - Main file: minerals_dashboard.py"
echo "   - Click Deploy!"
echo ""
echo "📖 Full guide: see DEPLOYMENT_GUIDE.md"

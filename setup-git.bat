@echo off
echo Setting up Git repository for Stochastic Control course...

REM Initialize git repository
git init

REM Add all files
git add .

REM Create initial commit
git commit -m "Initial commit: Add course structure and markdown templates"

echo.
echo Git repository initialized successfully!
echo.
echo Next steps:
echo 1. Create a new repository on GitHub
echo 2. Add the remote origin: git remote add origin [your-repo-url]
echo 3. Push to GitHub: git push -u origin main
echo.
echo Don't forget to fill in the markdown files with content from your PDFs!

pause
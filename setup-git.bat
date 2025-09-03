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
echo Adding remote origin and pushing to GitHub...
git remote add origin https://github.com/adityabn6/EECS-558.git
git branch -M main
git push -u origin main

echo.
echo Repository successfully pushed to GitHub!
echo URL: https://github.com/adityabn6/EECS-558
echo.
echo Don't forget to fill in the markdown files with content from your PDFs!

pause
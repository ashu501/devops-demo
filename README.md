# DevOps CI/CD Demo Project

A simple project to demonstrate a working CI/CD pipeline using **GitHub Actions**.

## What's in this project
- `app.py` — a small Python app with a few functions
- `test_app.py` — unit tests for those functions (run automatically by the pipeline)
- `index.html` — a simple webpage
- `.github/workflows/ci-cd.yml` — the CI/CD pipeline definition
- `requirements.txt` — Python dependencies (pytest)

## How the pipeline works
Every time you `git push` to the `main` branch (or open a pull request into `main`):
1. GitHub Actions spins up a fresh Ubuntu virtual machine
2. Checks out your code
3. Installs Python and dependencies
4. Runs all unit tests (`pytest`)
5. Runs the app
6. If everything passes, the `deploy` job runs (currently a placeholder)

## How to set this up on your own GitHub account

1. Create a new repository on GitHub (e.g., `devops-demo-project`)
2. In your terminal, inside this folder:
   ```
   git init
   git add .
   git commit -m "Initial commit: CI/CD demo project"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/devops-demo-project.git
   git push -u origin main
   ```
3. Go to your repository on GitHub → click the **Actions** tab
4. You'll see the pipeline run automatically — green check = success

## How to demonstrate this live in class
1. Show the repo's **Actions** tab with a passing pipeline (green checkmark)
2. Open `test_app.py` and break a test on purpose (e.g., change `assert add(2, 3) == 5` to `== 6`)
3. Commit and push the change
4. Show the pipeline **failing** (red X) in the Actions tab, and open the logs to show the exact error
5. Fix the test, commit, push again — show the pipeline turning green again

This demonstrates the core CI/CD idea: **every change is automatically tested before it's considered "good."**

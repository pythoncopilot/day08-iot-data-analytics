## GitHub Actions (CI Pipeline)

This project uses GitHub Actions to automatically validate Python code on every push.

### Workflow Steps:
1. GitHub detects push to main branch
2. Creates a fresh Linux runner
3. Installs Python 3.11
4. Runs compile check on all Python files

### What it checks:
- Python syntax errors
- File structure validity
- Basic code integrity

### What it does NOT check:
- Runtime execution
- Database connections
- API responses
- UI behavior

### Why CI is important:
- Prevents broken code from being merged
- Provides instant feedback after commits
- Ensures code quality consistency
- Simulates real production pipelines

### View results:
Go to the "Actions" tab in GitHub repository.
Each push generates a new workflow run.

## 🚀 Level 2 CI Pipeline (IoT System Validation)

This project uses an advanced GitHub Actions workflow to validate not only Python syntax but also IoT system behavior.

---

## 🔧 What Level 2 CI does

Every push triggers the following automated checks:

### 1. Python Code Validation
- Runs `python -m compileall`
- Ensures all Python files are syntactically correct
- Detects indentation and structure errors

---

### 2. IoT Analytics Execution
- Automatically runs `analytics.py`
- Simulates real IoT data analysis in CI environment
- Validates that database queries and logic work correctly

---

### 3. Infrastructure Validation
- Checks if required project folders exist
- Ensures project structure integrity (database, python, etc.)

---

## 🧠 What this means

Instead of only checking code quality, CI now verifies:

- Code correctness
- System logic execution
- Basic IoT workflow behavior

---

## 🔁 CI Pipeline Flow

GitHub Push → GitHub Actions Runner →  
Python Setup → Syntax Check → Analytics Run → Structure Validation → Result

---

## ⚠️ Important Notes

- Each GitHub Action runs in a fresh environment
- Database is not persistent between runs
- CI is used only for validation, not production data storage

---

## 🚀 Current CI Level

**Level 2: IoT System Validation Pipeline**

Next upgrade will include:
- API endpoint testing
- Real sensor simulation in CI
- JSON response validation
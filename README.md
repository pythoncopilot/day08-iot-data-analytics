# Day 8 — IoT Data Analytics & Event-Driven CI Pipeline

This project is part of a 30-day Embedded Systems Learning Journey.

Day 8 focuses on:
- IoT data analytics
- SQLite-based event tracking
- real-time dashboard integration
- event-driven GitHub Actions CI pipeline

---

# 🧠 Project Overview

This system simulates a Smart Home IoT ecosystem:

Arduino (simulated)
   ↓
Python Backend (Flask API)
   ↓
SQLite Database (data storage)
   ↓
Analytics Engine (data insights)
   ↓
Web Dashboard (UI control panel)

---

# ⚙️ Features

## 🔌 IoT System
- Device control simulation (light, fan, AC, etc.)
- REST API using Flask
- Real-time state updates

## 🗄️ Database Layer
- SQLite database storage
- Logs all device control actions
- Stores timestamped events

## 📊 Analytics Engine
- Total device activity tracking
- Most frequently used devices
- Recent activity logs
- IoT behavior insights

## 🌐 Dashboard
- Web-based control interface
- Real-time device interaction
- Live status updates

---

# 🚀 GitHub Actions CI Pipeline (Level 3)

This project includes an event-driven CI system using GitHub Actions.

---

## ⚙️ CI Trigger Rules

The pipeline runs ONLY when changes occur in:

- `python/` → backend logic updates
- `dashboard/` → UI changes
- `arduino/` → embedded system code
- `database/` → data structure updates

---

## ❌ Ignored Changes

CI does NOT run when:

- `README.md` is updated
- documentation changes only
- non-functional file edits

This improves efficiency and avoids unnecessary builds.

---

## 🔁 CI Pipeline Flow

Git Push
   ↓
GitHub checks changed files
   ↓
If relevant code changed:
   ↓
GitHub Actions runner starts
   ↓
Python environment setup
   ↓
Code validation & execution
   ↓
Analytics script runs
   ↓
Structure verification
   ↓
Result (PASS / FAIL)

---

## 🧪 CI Checks Performed

### 1. Python Syntax Validation
- Uses `compileall`
- Ensures no syntax errors in backend code

### 2. IoT Analytics Execution
- Runs `analytics.py`
- Simulates real IoT data analysis in CI environment

### 3. Project Structure Validation
- Ensures required folders exist:
  - python/
  - dashboard/
  - arduino/
  - database/

---

# 🧠 Why This Matters

This project demonstrates a real-world DevOps pattern:

Event-Driven Continuous Integration (CI)

It ensures:
- Efficient CI execution
- Reduced unnecessary builds
- Faster feedback cycles
- Production-style automation workflow

---

# 📊 Current System Level

Level 3: Event-Driven IoT CI Pipeline

---

# 🔮 Future Improvements (Day 9+)

Planned upgrades:
- API endpoint testing inside CI
- Real sensor simulation in GitHub Actions
- JSON response validation
- Full IoT system automated testing pipeline
- Performance and reliability checks

---

# 🛠️ How to Run Locally

## 1. Start backend API
python python/api.py

## 2. Open dashboard
dashboard/index.html

## 3. Run analytics
python python/analytics.py

## 4. (Optional) Simulate IoT data
python python/serial_reader.py

---

# 📌 Learning Goals Achieved

- IoT system architecture design
- SQLite integration for real-time logging
- Python-based analytics engine
- Web dashboard control system
- Introduction to GitHub Actions CI/CD
- Event-driven automation concepts

---

# 🚀 Summary

Day 8 introduces the transition from:

IoT System → IoT + Data Intelligence + CI Automation

This is a key step toward production-level embedded systems development.
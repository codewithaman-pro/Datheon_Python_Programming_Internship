# Python Programming Internship - Datheon

Welcome to my official **Python Programming Internship** repository for **Datheon**. This project showcases an enterprise-grade suite of modular applications, console-based games, financial automation tools, filesystem utilities, conversational AI engines, and object-oriented inventory systems.

---

## 📌 Project Overview

All five tasks within this repository are built with clean code practices, structural encapsulation, error handling, strict adherence to Python's standard library documentation, and modular execution.

---

## 🛠️ Repository Structure

```text
Python Hangman Internship/
│
├── hangman.py                 # Task 1: Interactive Hangman Word Game
├── portfolio.py               # Task 2: Stock Portfolio Performance Tracker
├── organizer.py               # Task 3: Automated File Organizer & Cleanup Utility
├── chatbot.py                 # Task 4: Rule-Based Interactive Terminal Assistant
├── inventory.py               # Task 5: OOPs Enterprise Smart Inventory System
│
├── sample_faq (2).json        # JSON Dataset for Task 4 Chatbot
├── portfolio_summary.csv      # Output logs for Task 2 Portfolio Tracker
└── README.md                  # Project Documentation
```

---

## 📋 Included Tasks & Key Features

### Task 1: Hangman Word Guessing Game (`hangman.py`)
* **Goal**: Build an interactive, modular console game demonstrating string manipulation and state management.
* **Key Features**:
  * Random word selection from predefined categories.
  * Interactive turn-based interface displaying remaining lives and guessed letters.
  * Real-time ASCII art representation of hangman stages.

### Task 2: Stock Portfolio Performance Tracker (`portfolio.py`)
* **Goal**: Real-time portfolio valuation engine with automated transaction logging.
* **Key Features**:
  * Calculation of total invested capital, current valuation, and overall PnL (Profit & Loss).
  * Industry sector distribution calculation.
  * Automated CSV logging (`portfolio_summary.csv`) using Python’s native `csv` library.

### Task 3: Automated File Organizer & Cleanup Utility (`organizer.py`)
* **Goal**: Autonomous filesystem automation utility utilizing Python `os` and `shutil` libraries.
* **Key Features**:
  * Scans target directories using `os.scandir()` for high-performance iteration.
  * Automatically categorizes extensions into clean structure (`/Documents`, `/Images`, `/Videos`, `/Archives`, `/Code`).
  * Robust error handling for `PermissionError` and file path collisions.

### Task 4: Rule-Based Interactive Terminal Assistant (`chatbot.py`)
* **Goal**: Conversational chatbot with regular expression intent recognition.
* **Key Features**:
  * Reads knowledge base dynamically from `sample_faq (2).json`.
  * Regex matching using `re` module for greeting detection and contextual responses.
  * Graceful fallback mechanisms and keyboard interrupt handling.

### Task 5: OOPs Architecture Enterprise Smart Inventory System (`inventory.py`)
* **Goal**: Production-grade inventory and asset management system using OOP design principles.
* **Key Features**:
  * Abstract base class `LibraryItem` via Python `abc` module.
  * Concrete child classes (`Book`, `Magazine`, `DigitalMedia`) implementing polymorphism.
  * Encapsulated private/protected fields with property getters/setters.
  * Dunder method overrides (`__str__`, `__repr__`, `__eq__`) for clean data representation.

---

## ⚙️ How to Run

### Prerequisites
* Python 3.8 or higher installed on your local machine.

### Execution Instructions
Run any individual task directly from your terminal:

```bash
# Task 1: Hangman Game
python hangman.py

# Task 2: Portfolio Tracker
python portfolio.py

# Task 3: File Organizer
python organizer.py

# Task 4: Terminal Chatbot
python chatbot.py

# Task 5: Inventory System
python inventory.py
```

---

## 👤 Author
* **Intern Name**: Aman
* **Internship Program**: Python Programming Internship (Datheon)
* **GitHub**: [code with aman pro](https://github.com)

---
*Submitted for Datheon Internship Certification Review.*
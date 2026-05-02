# 📧 Spam Email Classifier

A Python-based email classifier that uses keyword scoring to determine whether an email is spam or legitimate (ham). No external libraries required — runs with pure Python.

## Features
- Classifies emails as **SPAM** or **HAM**
- Shows confidence percentage
- Highlights matched spam/ham keywords
- Built-in demo mode with 4 sample emails
- Option to classify your own custom email

## How to Run
1. Make sure Python is installed
2. Download `spam_classifier.py`
3. Open terminal and run:
```bash
python spam_classifier.py
```
4. Choose to test your own email or run the demo

## How It Works
- Preprocesses email text (lowercase)
- Scores against a list of known spam keywords (e.g. "free", "winner", "act now")
- Scores against legitimate email keywords (e.g. "meeting", "report", "deadline")
- Classifies based on score thresholds with a confidence level

## Tech Used
- **Language:** Python
- **Concepts:** NLP basics, keyword matching, text preprocessing, scoring logic, functions

## Author
**Inamdar Mohammad Ali**  
B.E. Computer Science (AI & ML) — M.H. Saboo Siddiq College of Engineering, Mumbai

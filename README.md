# Expense Tracker CLI

A Python-based command-line application for managing and tracking personal expenses.

## Features

- Add expenses
- View all expenses
- Search expenses
- Calculate total expenses
- Delete expenses
- Store expense data in JSON format
- Display expenses using a formatted CLI table

## Installation

Create and activate a virtual environment:

```bash
python -m venv .venv
Install the required dependencies:

pip install -r requirements.txt
How to Run

From the project root directory:

python -m app.main
Project Structure
expense-tracker-cli/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── services.py
│   └── storage.py
├── data/
│   └── expenses.json
├── requirements.txt
├── .gitignore
└── README.md
Technologies Used
Python
JSON
Rich
Purpose

This project was built to practice Python CLI application development, file handling, data storage, and modular project organization.

import json
from dataclasses import asdict
from pathlib import Path

from app.models import Expense


DATA_FILE = Path("data/expenses.json")


def load_expenses():
    if not DATA_FILE.exists():
        return []

    with DATA_FILE.open("r") as file:
        data = json.load(file)

    return [Expense(**item) for item in data]


def save_expenses(expenses):
    with DATA_FILE.open("w") as file:
        data = [asdict(expense) for expense in expenses]
        json.dump(data, file, indent=4)
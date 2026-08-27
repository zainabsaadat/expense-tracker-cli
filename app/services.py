from app.models import Expense


def add_expense(expenses, title, amount, category):
    expense = Expense(title, amount, category)
    expenses.append(expense)
    return expenses


def calculate_total(expenses):
    return sum(expense.amount for expense in expenses)


def search_expenses(expenses, keyword):
    return [
        expense
        for expense in expenses
        if keyword.lower() in expense.title.lower()
        or keyword.lower() in expense.category.lower()
    ]


def delete_expense(expenses, title):
    for expense in expenses:
        if expense.title.lower() == title.lower():
            expenses.remove(expense)
            return True

    return False

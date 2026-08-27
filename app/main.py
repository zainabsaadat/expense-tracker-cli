from rich.console import Console
from rich.table import Table

from app.services import (
    add_expense,
    calculate_total,
    search_expenses,
    delete_expense,
)
from app.storage import load_expenses, save_expenses


console = Console()


def show_menu():
    console.print("\n[bold cyan]===== EXPENSE TRACKER =====[/bold cyan]")
    console.print("1. Add Expense")
    console.print("2. View All Expenses")
    console.print("3. Search Expense")
    console.print("4. Calculate Total")
    console.print("5. Delete Expense")
    console.print("6. Exit")


def display_expenses(expenses):
    if not expenses:
        console.print("[yellow]No expenses found.[/yellow]")
        return

    table = Table(title="Your Expenses")

    table.add_column("Title")
    table.add_column("Amount")
    table.add_column("Category")

    for expense in expenses:
        table.add_row(
            expense.title,
            f"{expense.amount:.2f}",
            expense.category,
        )

    console.print(table)


def main():
    expenses = load_expenses()

    while True:
        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter expense title: ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")

            expenses = add_expense(
                expenses,
                title,
                amount,
                category,
            )

            save_expenses(expenses)
            console.print("[green]Expense added successfully![/green]")

        elif choice == "2":
            display_expenses(expenses)

        elif choice == "3":
            keyword = input("Enter search keyword: ")
            results = search_expenses(expenses, keyword)
            display_expenses(results)

        elif choice == "4":
            total = calculate_total(expenses)
            console.print(f"[bold green]Total: {total:.2f}[/bold green]")

        elif choice == "5":
            title = input("Enter expense title to delete: ")

            if delete_expense(expenses, title):
                save_expenses(expenses)
                console.print("[green]Expense deleted successfully![/green]")
            else:
                console.print("[red]Expense not found.[/red]")

        elif choice == "6":
            console.print("[cyan]Goodbye![/cyan]")
            break

        else:
            console.print("[red]Invalid choice.[/red]")


if __name__ == "__main__":
    main()
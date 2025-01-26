import os
import datetime

class ExpenseTracker:
    """
    A simple personal expense tracker.
    """

    def __init__(self):
        """
        Initializes the expense tracker with an empty list of expenses.
        """
        self.expenses = []
        self.budget = 0

    def add_expense(self, amount, category, date=None):
        """
        Adds a new expense to the list.

        Args:
            amount (float): The amount of the expense.
            category (str): The category of the expense.
            date (str or datetime.date): The date of the expense (optional). 
                If not provided, uses today's date.
        """
        if date is None:
            date = datetime.date.today()
        self.expenses.append({'amount': amount, 'category': category, 'date': date})

    def view_expenses(self):
        """
        Displays all expenses in a table format.
        """
        if not self.expenses:
            print("No expenses found.")
            return

        headers = ['Date', 'Category', 'Amount']
        print("{:<25} {:<25} {:>10}".format(*headers))
        print("-" * 62)
        for expense in self.expenses:
            print("{:<25} {:<25} {:>10.2f}".format(
                expense['date'].strftime('%Y-%m-%d'), 
                expense['category'], 
                expense['amount']))

    def view_expenses_by_category(self, category):
        """
        Displays expenses for a specific category.

        Args:
            category (str): The category to filter by.
        """
        category_expenses = [
            expense for expense in self.expenses 
            if expense['category'] == category]

        if not category_expenses:
            print(f"No expenses found in '{category}' category.")
            return

        print(f"Expenses in '{category}' category:")
        self.view_expenses()  # Use the existing view_expenses method

    def set_monthly_budget(self, budget):
        """
        Sets the monthly budget.

        Args:
            budget (float): The monthly budget amount.
        """
        self.budget = budget

    def get_total_expenses(self):
        """
        Calculates the total expenses.
        """
        return sum(expense['amount'] for expense in self.expenses)

    def get_remaining_budget(self):
        """
        Calculates the remaining budget.
        """
        return self.budget - self.get_total_expenses()

    def save_expenses(self, filename):
        """
        Saves expenses to a file.

        Args:
            filename (str): The name of the file to save to.
        """
        with open(filename, 'w') as file:
            for expense in self.expenses:
                date_str = expense['date'].strftime('%Y-%m-%d')
                file.write(f"{expense['amount']},{expense['category']},{date_str}\n")

    def load_expenses(self, filename):
        """
        Loads expenses from a file.

        Args:
            filename (str): The name of the file to load from.
        """
        if not os.path.exists(filename):
            print(f"File '{filename}' not found.")
            return

        self.expenses = []
        with open(filename, 'r') as file:
            for line in file:
                amount, category, date_str = line.strip().split(',')
                date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
                self.expenses.append({'amount': float(amount), 
                                       'category': category, 
                                       'date': date})

def main():
    """
    Main function to run the expense tracker.
    """
    tracker = ExpenseTracker()
    filename = 'expenses.txt'

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Expenses by Category")
        print("4. Set Monthly Budget")
        print("5. View Remaining Budget")
        print("6. Save Expenses")
        print("7. Load Expenses")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            date_str = input("Enter date (YYYY-MM-DD, optional): ")
            if date_str:
                date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
            else:
                date = None
            tracker.add_expense(amount, category, date)
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            category = input("Enter category: ")
            tracker.view_expenses_by_category(category)
        elif choice == '4':
            budget = float(input("Enter monthly budget: "))
            tracker.set_monthly_budget(budget)
        elif choice == '5':
            remaining_budget = tracker.get_remaining_budget()
            print(f"Remaining Budget: ${remaining_budget:.2f}")
        elif choice == '6':
            tracker.save_expenses(filename)
            print(f"Expenses saved to {filename}")
        elif choice == '7':
            tracker.load_expenses(filename)
            print(f"Expenses loaded from {filename}")
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
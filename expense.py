import json
from datetime import datetime

# Expense Tracker Class
class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, description):
        try:
            expense = {
                'amount': float(amount),
                'category': category,
                'description': description,
                'date': datetime.now().strftime('%Y-%m-%d')
            }
            self.expenses.append(expense)
            print(f"Expense added: {description}, Amount: {amount}, Category: {category}")
        except ValueError:
            print("Invalid amount. Please enter a number.")

    def save_expenses(self, filename="expenses.json"):
        with open(filename, 'w') as file:
            json.dump(self.expenses, file)
        print(f"Expenses saved to {filename}.")

    def load_expenses(self, filename="expenses.json"):
        try:
            with open(filename, 'r') as file:
                self.expenses = json.load(file)
            print(f"Expenses loaded from {filename}.")
        except FileNotFoundError:
            print("No saved expenses found.")

    def monthly_summary(self):
        summary = {}
        for expense in self.expenses:
            month = expense['date'][:7]  # Extract year and month
            if month not in summary:
                summary[month] = 0
            summary[month] += expense['amount']
        print("\nMonthly Summary:")
        for month, total in summary.items():
            print(f"{month}: ${total:.2f}")

    def category_summary(self):
        summary = {}
        for expense in self.expenses:
            category = expense['category']
            if category not in summary:
                summary[category] = 0
            summary[category] += expense['amount']
        print("\nCategory-wise Summary:")
        for category, total in summary.items():
            print(f"{category}: ${total:.2f}")

# Main function for user interaction
def main():
    tracker = ExpenseTracker()
    tracker.load_expenses()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Monthly Summary")
        print("3. View Category-wise Summary")
        print("4. Save Expenses")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            amount = input("Enter amount: ")
            category = input("Enter category (e.g., food, transportation): ")
            description = input("Enter description: ")
            tracker.add_expense(amount, category, description)
        elif choice == '2':
            tracker.monthly_summary()
        elif choice == '3':
            tracker.category_summary()
        elif choice == '4':
            tracker.save_expenses()
        elif choice == '5':
            tracker.save_expenses()
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
  

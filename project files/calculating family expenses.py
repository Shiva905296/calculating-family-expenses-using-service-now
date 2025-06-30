# Family Expenses Calculator - Executable Python Code

# Sample family expenses data
family_expenses = [
    {'item': 'Groceries', 'amount': 5000},
    {'item': 'Electricity Bill', 'amount': 1200},
    {'item': 'Water Bill', 'amount': 300},
    {'item': 'School Fees', 'amount': 10000},
    {'item': 'Medical Expenses', 'amount': 2500},
    {'item': 'Transport', 'amount': 1500},
    {'item': 'Entertainment', 'amount': 2000}
]

# Function to calculate total expenses
def calculate_total_expenses(expenses):
    total = 0
    for expense in expenses:
        total += expense['amount']
    return total

# Function to display expenses
def display_expenses(expenses):
    print("Family Expenses:")
    for expense in expenses:
        print(f"{expense['item']}: ₹{expense['amount']}")
    print()

# Main process
def main():
    display_expenses(family_expenses)
    total = calculate_total_expenses(family_expenses)
    print(f"Total Family Expenses: ₹{total}")

if __name__ == "__main__":
    main()
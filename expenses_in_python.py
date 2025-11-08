expenses = []  # list to store expenses

def add_expense(description, amount):
    """Add a new expense to the list"""
    expenses.append({"description": description, "amount": float(amount)})      
    print("Expense added successfully!")
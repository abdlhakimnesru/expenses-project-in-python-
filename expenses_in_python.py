expenses = []  # list to store expenses

def add_expense(description, amount):
    expenses.append({"description": description, "amount": float(amount)})      
    print("Expense added successfully!")


def view_expenses():
    if not expenses:
        print("No expenses yet. Add one first!")
        return
    total = 0
    print("\nDescription      Amount")
    print("-"*25)
    for item in expenses:
        print(f"{item['description']:15}  ${item['amount']}")
        total += item['amount']
    print("-"*25)
    print(f"Total Spent: ${total}")
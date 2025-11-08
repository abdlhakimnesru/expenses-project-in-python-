# Simple Personal Expense Tracker python  project

expenses = []  # list to store expenses

def add_expense(description, amount):
    """Add a new expense to the list"""
    expenses.append({"description": description, "amount": float(amount)})      
    print("Expense added successfully!")

    

# def view_expenses():
#     """View all expenses and total spent"""
#     if not expenses:
#         print("No expenses yet. Add one first!")
#         return
#     total = 0
#     print("\nDescription      Amount")
#     print("-"*25)
#     for item in expenses:
#         print(f"{item['description']:15}  ${item['amount']}")
#         total += item['amount']
#     print("-"*25)
#     print(f"Total Spent: ${total}")



# def main():
#     while True:
#         print("\nSimple Expense Tracker")
#         print("1. Add Expense")
#         print("2. View Expenses")
#         print("3. Exit")
#         choice = input("Enter your choice: ")
#         if choice == "1":
#             desc = input("Enter description: ")
#             amt = input("Enter amount: ")
#             add_expense(desc, amt)
#         elif choice == "2":
#             view_expenses()
#         elif choice == "3":
#             print("Goodbye!")
#             break
#         else:
#             print("Invalid choice. Try again.")

# if __name__ == "__main__":
#     main()


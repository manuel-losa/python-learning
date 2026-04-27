def add_expense(expenses, name, amount):
    expense = {
        "name" : name,
        "amount" : amount 
    }

    expenses.append(expense)
    return expenses


def get_total(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total 


def show_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses yet")
        return
    
    for i, expense in enumerate(expenses):
        print(f"{i} - {expense['name']}: £{expense['amount']:.2f}")


def delete_expense(expenses, index):
    if index < 0 or index >= len(expenses):
        print("Invalid index")
        return expenses
    
    expenses.pop(index)
    return expenses
def add_expense(expenses, name, amount, category):
    expense = {
        "name": name,
        "amount": amount,
        "category": category
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
        print(f"{i} - {expense['name']} | {expense['category']} | £{expense['amount']:.2f}")


def delete_expense(expenses, index):
    if index < 0 or index >= len(expenses):
        print("Invalid index")
        return expenses
    
    expenses.pop(index)
    return expenses
    
def save_expenses(expenses):
    with open("expenses.txt", "w") as file:
        for expense in expenses:
            line = f"{expense['name']}, {expense['amount']}\n"
            file.write(line)

def load_expenses():
    expenses = []

    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                name, amount = line.strip().split(",")
                expenses.append({
                    "name": name,
                    "amount": float(amount)
                })
    except:
        pass

    return expenses
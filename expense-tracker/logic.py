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
            line = f"{expense['name']}, {expense['amount']}, {expense['category']}\n"
            file.write(line)

def load_expenses():
    expenses = []

    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                name, amount, category = line.strip().split(",")
                expenses.append({
                    "name": name,
                    "amount": float(amount),
                    "category": category
                })
    except:
        pass

    return expenses

def get_total_by_category(expenses):
    totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in totals:
            totals[category] += amount
        else:
            totals[category] = amount

    return totals

def show_totals_by_category(expenses):
    totals = get_total_by_category(expenses)

    if len(totals) == 0:
        print("No data")
        return
    
    for category, total in totals.items():
        print(f"{category}: £{total:.2f}")
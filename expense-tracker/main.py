from logic import add_expense, get_total, show_expenses, delete_expense, save_expenses, load_expenses, show_totals_by_category


def main():
    expenses = load_expenses()

    while True:
        print("\n=== EXPENSE TRACKER ===")
        print("1. Add expense")
        print("2. Show expenses")
        print("3. Show total")
        print("4. Exit")
        print("5. Delete expense")
        print("6. Show totals by category")

        option = input("Choose: ")

        if option == "1":
            name = input("Expense name: ")
            try:
                amount = float(input("Amount: "))
            except: 
                print("Invalid amount")
                continue

            category = input("Category: ")

            add_expense(expenses, name, amount, category)
            save_expenses(expenses)

        elif option == "2":
            show_expenses(expenses)

        elif option == "3":
            total = get_total(expenses)
            print(f"Total: £{total:.2f}")

        elif option == "4":
            print("Good bye")
            break

        elif option == "5":
            show_expenses(expenses)

            try:
                index = int(input("Enter index to delete: "))

            except:
                print("Invalid number")
                continue

            delete_expense(expenses, index)
            save_expenses(expenses)

        elif option == "6":
            show_totals_by_category(expenses)

        else:
            print("Invalid option")
        

if __name__ == "__main__":
    main()
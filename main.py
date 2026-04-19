from logic import analyze_age, analyze_income, analyze_savings 

def get_number(prompt):
    while True:
        value = input(prompt)

        if value.isdigit():
            return int(value)
        else:
            print("Please enter a valid number.")

def show_result(label, result):
    print(label, result)



options = [
    "1. Check income",
    "2. Check age",
    "3. Check savings",
    "4. Exit"
]

def handle_income():
    income = get_number("Income: ")
    show_result("Income:", analyze_income(income))

def handle_age():
    age = get_number("Age: ")
    show_result("Age:", analyze_age(age))

def handle_savings():
    savings = get_number("Savings: ")
    show_result("Savings:", analyze_savings(savings))

actions = {
    "1": handle_income,
    "2": handle_age,
    "3": handle_savings
}

def main ():
    while True:
        print("\n=== DASHBOARD ===")
        for option_text in options:
            print(option_text)

        option = input("Choose: ")

        if option in actions:
            actions[option]()

        elif option == "4":
            print("Good bye")
            break

        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
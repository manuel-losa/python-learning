from logic import analyze_age, analyze_income, analyze_savings 


def main ():
    while True:
        print("\n=== DASHBOARD ===")
        print("1. Check income")
        print("2. Check age")
        print("3. Check savings")
        print("4. Exit")

        option = input("Choose: ")

        if option == "1":
            income = int(input("Income: "))
            print(analyze_income(income))

        elif option == "2":
            age = int(input("Age: "))
            print(analyze_age(age))

        elif option == "3":
            savings = int(input("Savings: "))
            print(analyze_savings(savings))

        elif option == "4":
            print("Good bye")
            break

        else:
            print("Invalid option")

main()
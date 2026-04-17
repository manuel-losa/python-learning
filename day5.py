def analyze_income(income):
    if income < 20000:
        return "Low income"
    elif income < 50000:
        return "Stable income"
    else:
        return "Strong position"


def analyze_age(age):
    if age < 18:
        return "Minor"
    elif age < 35:
        return "Young adult"
    else:
        return "Adult"


def analyze_savings(savings):
    if savings < 1000:
        return "Low savings"
    elif savings < 10000:
        return "Good savings"
    else:
        return "Strong savings"


def main():
    while True:
        print("\n=== DASHBOARD ===")
        print("1. Check income")
        print("2. Check age")
        print("3. Check savings")
        print("4. Check full profile")
        print("5. Exit")

        option = input("Choose: ")

        if option == "1":
            income = int(input("Enter income: "))
            print("Result:", analyze_income(income))

        elif option == "2":
            age = int(input("Enter age: "))
            print("Result:", analyze_age(age))

        elif option == "3":
            savings = int(input("Enter savings: "))
            print("Result:", analyze_savings(savings))

        elif option == "4":
            age = int(input("Age: "))
            income = int(input("Income: "))
            savings = int(input("Savings: "))

            print("\n--- FULL PROFILE ---")
            print("Age:", analyze_age(age))
            print("Income:", analyze_income(income))
            print("Savings:", analyze_savings(savings))

        elif option == "5":
            print("Goodbye 👋")
            break

        else:
            print("Invalid option")


main()
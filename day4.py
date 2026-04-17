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
    

def main():
    while True:
        print("\n=== DASHBOARD ===")
        print("1. Check income")
        print("2. Check age")
        print("3. Exit")

        option = input("Choose ")

        if option == "1":
            income = int(input("Enter income: "))
            print("Result:", analyze_income(income))

        elif option == "2":
            age = int(input("Enter age: "))
            print("Result:", analyze_age(age))

        elif option == "3":
            print("Goodbye")
            break

        else:
            print("Invalid option")

main()
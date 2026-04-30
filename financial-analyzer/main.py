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

def calculate_total(prices):
    total = 0

    for price in prices:
        total += price

    return total 

def increase_prices(prices, multiplier):
    new_prices = []

    for price in prices:
        new_prices.append(round(price * multiplier, 2))

    return new_prices

def get_prices():
    prices_input = input("Enter prices separated by commas: ")
    prices = prices_input.split(",")

    try:
        prices = [round(float(price.strip()), 2) for price in prices]
        return prices
    except:
        print("Invalid input, please enter numbers only")
        return None
    
def get_multiplier():
    try:
        return float(input("Multiplier (e.g. 1.2 or 0.8): "))
    except: 
        print("Invalid multiplier")
        return None 
    
def calculate_difference(original_total, new_total):
    return round(original_total - new_total, 2)

def display_results(prices, result, original_total, new_total):
    print("Original prices:", prices)
    print("Original total: £", round(original_total, 2))

    print("New prices:", result)
    print("New total: £", round(new_total, 2))

    difference = calculate_difference(original_total, new_total)

    if difference > 0:
        print("You save: £", difference)
    else:
        print("You spend more: £", abs(difference))

def handle_prices():
    prices = get_prices()

    if prices is None:
        return

    if len(prices) == 0:
        print("No prices entered")
        return

    for price in prices:
        if price < 0:
            print("Prices cannot be negative")
            return

    multiplier = get_multiplier()

    if multiplier is None:
        return 

    if multiplier <= 0:
        print("Multiplier must be greater than 0")
        return

    result = increase_prices(prices, multiplier)

    original_total = calculate_total(prices)
    new_total = calculate_total(result)

    display_results(prices, result, original_total, new_total)

    input("\nPress Enter to continue...")


options = [
    "1. Check income",
    "2. Check age",
    "3. Check savings",
    "4. Exit",
    "5. Calculate new prices"
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
    "3": handle_savings,
    "5": handle_prices
}

def main():
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
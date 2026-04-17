print("=== LIFE ADVISOR ===")

age = int(input("How old are you? "))
income = int(input("How much do you earn per year? "))

print("\n--- ANALYSIS ---")

if age < 18:
    print("Stage: Learning phase")
    print("Focus: Build skills, not income yet")

elif income < 20000:
    print("Stage: Low income")
    print("Focus: Increase your income as soon as possible")

elif income < 50000:
    print("Stage: Stable but growing")
    print("Focus: Upgrade skills and increase income")

elif income >= 50000:
    print("Stage: Strong position")
    print("Focus: Invest or build assets")

    if income >= 80000:
        print("Level: Top tier")
        print("Focus: Freedom, scaling, investments")


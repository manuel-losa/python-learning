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
    
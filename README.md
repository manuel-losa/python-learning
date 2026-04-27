# 💰 Financial & Price Analyzer (Python)

A structured Python console application that analyzes financial data and calculates price adjustments using multipliers.

---

## 🚀 Key Features

* Income, age, and savings analysis
* Price calculation with multipliers
* Comparison between original and updated totals
* Detection of savings or overspending
* Input validation and error handling
* Clean and modular code structure

---

## 🧠 Application Flow

The program follows a real-world data processing pipeline:

1. User input
2. Data cleaning (`split`, `strip`, `float`)
3. Validation (empty input, negative values, invalid data)
4. Processing (calculations and transformations)
5. Output (clear and formatted results)

---

## 🛠️ Code Structure

The application is designed using modular functions:

* `get_prices()` → handles user input and parsing
* `get_multiplier()` → retrieves multiplier value
* `calculate_total()` → sums values
* `increase_prices()` → applies transformations
* `calculate_difference()` → computes savings or extra cost
* `display_results()` → handles output formatting
* `handle_prices()` → controls workflow

This separation improves readability, scalability, and maintainability.

---

## 🧪 Example

Input:
10, 20, 30
Multiplier: 0.8

Output:
Original total: £60.0
New total: £48.0
You save: £12.0

---

## 🧠 Skills Demonstrated

* Python fundamentals
* Data transformation and list processing
* Error handling (`try/except`)
* Input validation
* Clean code principles
* Functional decomposition
* Git version control

---

## ▶️ How to Run

```bash
python main.py
```

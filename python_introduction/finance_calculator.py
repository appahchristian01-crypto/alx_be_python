# finance_calculator.py

# Prompt the user for monthly income and expenses (exact prompts required)
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project savings after one year with 5% interest
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Helper to print integers without a trailing .0 when result is whole
def fmt(x):
    if isinstance(x, float) and x.is_integer():
        return str(int(x))
    return str(x)

# Output results in the required format
print(f"Your monthly savings are ${fmt(monthly_savings)}.")
print(f"Projected savings after one year, with interest, is: ${fmt(projected_savings)}.")

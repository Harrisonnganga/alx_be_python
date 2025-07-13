# Finance Calculator - Monthly Savings and Annual Projection

# User Input
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))


# Calculations
monthly_savings = monthly_income - monthly_expenses
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)

# Output Results
print(f"Your monthly savings: ${monthly_savings:.2f}")
print(f"Projected annual savings with 5% interest: KES {projected_savings:,.2f}")

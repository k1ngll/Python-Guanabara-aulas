# Ask for the house value, buyer's salary, and payment term
house_value = float(input("Enter the house value: $ "))
buyer_salary = float(input("Enter your monthly salary: $ "))
payment_years = int(input("Enter the payment term (in years): "))

# Calculate the monthly installment
payment_months = payment_years * 12
monthly_installment = house_value / payment_months

# Check if the monthly installment exceeds 30% of the salary
salary_limit = buyer_salary * 0.3
if monthly_installment <= salary_limit:
    print("Loan approved!")
    print(f"Monthly installment: $ {monthly_installment:.2f}")
else:
    print("Loan denied. The monthly installment exceeds 30% of your salary.")
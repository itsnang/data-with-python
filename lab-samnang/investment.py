amount = eval(input("Enter investment amount: "))
interest_rate = eval(input("Enter annual interest rate: "))
amount_year = eval(input("Enter number of years: "))

monthly_interest_rate = interest_rate / 1200
convert_year_to_month = amount_year * 12

future_investment_value = amount * (1 + monthly_interest_rate) ** convert_year_to_month

print("Accumulated value is",future_investment_value)

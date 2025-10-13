number_of_days = eval(input("Enter the number of days: "))

years = number_of_days // 365
months = (number_of_days % 365) // 30
days = number_of_days % 365 % 30
print('Years = ', years)
print('Months = ', months)
print('Days = ', days)

income = eval(input("Enter your annual income: "))

if income <= 10000:
    tax = 0.00
    print("The tax is", tax)
elif income >= 10001 or income <= 20000:
    tax = (income - 10000) * 0.1
    print("The tax is", tax)
elif income >= 20001 or income >= 50000:
    tax = 1000 + (income * 0.20) * 0.2
    print("The tax is", tax)
else:
    tax = 7000 + (income - 50000) * 0.3
    print("The tax is", tax)

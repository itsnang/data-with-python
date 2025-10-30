rate = eval(input("Enter exchange rate from dollars to RMB: "))
exchangeType = eval(input("Enter 0 to convert dollars to RMB and 1 vice versa: "))

if exchangeType == 0:
    amount = eval(input("Enter the dollar amount: "))
    convertedAmount = amount * rate
    print("$", amount, "is", convertedAmount, "yuan")
elif exchangeType == 1:
    amount = eval(input("Enter the RMB amount: "))
    convertedAmount = amount / rate
    print(amount, "yuan is $", convertedAmount)
else:
    print("Invalid input")

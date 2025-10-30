number1 = eval(input("Enter first number: "))
number2 = eval(input("Enter second number: "))
number3 = eval(input("Enter third number: "))
numbers = [number1, number2, number3]
average = sum(numbers) / len(numbers)
print(f"The average of {' '.join(map(str, numbers))} is: {average}")

operations = ["+", "-", "*", "/"]

inputNumber1 = eval(input("Enter the first number: "))
inputNumber2 = eval(input("Enter the second number: "))
operation = input("Enter the operator(+,-,*,/): ")


if(operation not in operations):
  print("Invalid operation entered.")
else:
  if(operation == "+"):
    result = inputNumber1 + inputNumber2
  elif(operation == "-"):
    result = inputNumber1 - inputNumber2
  elif(operation == "*"):
    result = inputNumber1 * inputNumber2
  elif(operation == "/"):
    result = inputNumber1 / inputNumber2

  print(f"The result is {result}")

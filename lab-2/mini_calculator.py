def arithmetic_operation (value1, value2, operation):
  operations = ["Addition", "Subtraction", "Multiplication", "Division"]
  while(operation not in operations):
    print("Invalid operation entered.")
    operation = input("Enter the operation(Addition, Subtraction, Multiplication, Division): ")
  if(operation == "Addition"):
    result = value1 + value2\

  elif(operation == "Subtraction"):
    result = value1 - value2

  elif(operation == "Multiplication"):
    result = value1 * value2

  elif(operation == "Division"):
    result = value1 / value2
  return result

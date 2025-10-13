number1, number2, number3 = eval(input("Enter three integers: "))

if(number1 > number2):
  number1, number2 = number2, number1
if(number1 > number3):
  number1, number3 = number3, number1
if(number2 > number3):
  number2, number3 = number3, number2

print("The sorted numbers are",number1, number2, number3)

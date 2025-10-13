num1, num2, num3 = eval(input("Enter three numbers: "))

if(num1 > num2):
    num1, num2 = num2, num1
if(num1 > num3):
    num1, num3 = num3, num1
if(num2 > num3):
    num2, num3 = num3, num2

print("The sorted numbers are:", num1, num2, num3)

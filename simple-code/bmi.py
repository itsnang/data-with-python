weight = eval(input("Enter your weight in kilograms: "))
height = eval(input("Enter your height in meters: "))

bmi = weight / (height * height)

underweight = bmi < 18.5
normal =  bmi <= 24.9
over_weight = bmi > 25.0 and bmi <= 29.9
obese = bmi > 30.0

if(underweight):
  print("You are underweight")
elif(normal):
  print("You are normal")
elif(over_weight):
  print("You are over weight")
elif(obese):
  print("You are obese")

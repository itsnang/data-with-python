import math
pi = math.pi


def getPositiveNumber(prompt):
  while True:
     try:
        value = eval(input(prompt))
        if(value <= 0):
          print("The number must be positive")
          continue
        else:
            return value
     except ValueError:
        print("Invalid input")



radius = getPositiveNumber("Enter the radius of the cylinder: ")
height = getPositiveNumber("Enter the height of the cylinder: ")


area = radius * radius * pi
volume = area * height
print("The area of the cylinder is: ", area)
print("The volume of the cylinder is: ", volume)

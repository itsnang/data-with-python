# def getPositiveNumber(prompt):
#        try:
#         value = eval(input(prompt))
#         if(value >0):
#           print('The number is positive')
#           return value
#         else:
#             print('The number is not positive')
#             return value
#        except ValueError:
#         print('Invalid input')

# inputNumber = getPositiveNumber('Enter a number: ')

inputNumber = eval(input('Enter a number: '))
if(inputNumber > 0):
    print(inputNumber, "is positive number")
else:
    print(inputNumber, "is negative number")

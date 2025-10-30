
# idNumber =123
# has_id = False

# inputAge = eval(input('Enter your age: '))
# inputIdNumber = eval(input('Enter your id number: '))

# if(inputIdNumber == idNumber):
#     has_id = True
# else:
#     has_id = False


# if(inputAge >= 18):
#     if has_id == True:
#       print('You are eligible to enter.')
#     else:
#       print('You are not eligible to enter.')
# else:
#   print('You are not old enough to enter.')


inputNumber = eval(input('Enter a number: '))

if(inputNumber % 2 == 0):
  if(inputNumber > 10):
    print('The number is even and greater than 10')
  else:
    print('The number is even and 10 or less.')
else:
  print("The number is odd")

numbers = [11,21,27,32,35,42,46,49,56,777]

for number in numbers:
  if(number > 50):
    continue
  elif(number>500):
    break
  if(number % 7 == 0):
    print(number)

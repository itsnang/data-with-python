numbers = [5,-3,8,-1,10]

sum = 0
for number in numbers:
  is_negative = number < 0
  if(is_negative):
    continue
  else:
    sum += number
print('The sum of positive numbers is:', sum)

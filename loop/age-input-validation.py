age = eval(input('Enter your age:'))

negative_num = age < 0

while negative_num:
  age = eval(input('Age value canoot be nagative. Enter your age:'))
  if(negative_num):
    break
print('You are', age, 'year old.')

numbers = eval(input('Enter a number:'))
multipliers = [1,2,3,4,5,6,7,8,9]

print('Number\tMultiplier\tProduct')
result = 0

for multi in multipliers:
      result *= multi
      print(numbers, multi, result)

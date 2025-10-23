def get_grade(score):
  if(score>= 90):
    return 'A'
  elif(score >= 80):
    return 'B'
  elif(score>=70):
    return 'C'
  elif (score>=60):
    return 'D'
  else:
    return 'F'

score = eval(input('Enter your score:'))
print('Your grade is', get_grade(score))

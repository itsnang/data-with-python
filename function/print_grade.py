def grade (score):
  if(score >= 90):
    print('A')
  # TODO: handle another score
  else:
    print('F')

score = eval(input('Enter your score:'))

grade(score)

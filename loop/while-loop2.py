correct_anws = 1
ans = eval(input('What is 4-1:'))


count_user = 0
while ans != correct_anws:
  ans = eval(input('Wrong answer. try again:'))
  count_user += 1
  if count_user == 3:
    print('You are reach limit')
    break
if ans == correct_anws:
    print('You got it')

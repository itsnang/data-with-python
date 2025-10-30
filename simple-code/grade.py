from enum import Enum

class Grade(Enum):
  A = "A"
  B = "B"
  C = "C"
  D = "D"
  F = "F"
score = eval(input("Enter your score: "))
name = input("Enter your name: ")

def getScore(score):
  if(score >= 90):
    return Grade.A.value
  elif(score >= 80):
    return Grade.B.value
  elif(score >= 70):
    return Grade.C.value
  elif(score >= 60):
    return Grade.D.value
  else:
    return Grade.F.value

print('Your name',name,'and get', getScore(score), 'grade')

import random

PW = input('PASSWORD=? ')
PW = int(PW)
RPW = random.randint(1, 100)

while True:
  if PW == RPW:
    print('YOU GOT IT!')
    break
  elif PW > RPW:
    print('BIGGER THAN ANSWER')
  elif PW < RPW:
    print('LESS THAN ANSWER')

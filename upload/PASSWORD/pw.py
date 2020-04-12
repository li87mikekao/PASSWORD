import random
COUNT = 0
PW = input('PASSWORD=? ')
PW = int(PW)
RPW = random.randint(1, 100)
while True:
  COUNT = COUNT + 1
  if PW == RPW:
    print('YOU GOT IT! TRIED',COUNT,'TIMES!')
    break
  elif PW > RPW:
    print('BIGGER THAN ANSWER')
  elif PW < RPW:
    print('LESS THAN ANSWER')
  print('TRIED',COUNT,'TIMES!')

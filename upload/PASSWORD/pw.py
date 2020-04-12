import random
COUNT = 0
START = input('START FROM ')
START = int(START)
END = input('END AT ')
END = int(END)
RPW = random.randint(START, END)
while True:
  PW = input('PASSWORD=? ')
  PW = int(PW)
  COUNT = COUNT + 1
  if PW == RPW:
    print('YOU GOT IT! TRIED',COUNT,'TIMES!')
    break
  elif PW > RPW:
    print('BIGGER THAN ANSWER')
  elif PW < RPW:
    print('LESS THAN ANSWER')
  print('TRIED',COUNT,'TIMES!')

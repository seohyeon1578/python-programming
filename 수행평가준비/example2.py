# 2. 연도와 월을 알고 있을 때 그 달의 마지막 날을 구하는 프로그램을 작성하세요.
# --- 조건 1 : 400의 배수인 해는 모두 윤년이다.
# --- 조건 2 : 4의 배수인 해들 중 100의 배수가 아닌 해들은 모두 윤년이다.

y, m = map(int, input().split(' '))
leapYear = False
if((y % 4 == 0 and y % 100 != 0) or y % 400 == 0): 
  leapYear = True 
else: 
  leapYear = False

if(m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
  print('31')
elif(m == 2):
  if(leapYear):
    print('29')
  else:
    print('28')
else:
  print('30')
# 3. 입력 값 a와 b사이에 존재하는 자연수(a, b 포함)에 대해서 홀수는 더하고, 짝수는 빼는 식을 보여준 후 결과를 출력하세요.
# --- 입력조건: 0 < a <= b <= 500
# --- 입력예시: 5 10

isInput = True
while(isInput):
  a, b = map(int, input().split(' '))
  if(a > 0 and b > 0 and a <= b and b <= 500):
    isInput = False
  else:
    print('다시입력해주세요.')
    print('입력조건: 0 < a <= b <= 500')

sum = 0
for i in range(a, b + 1):
  if(i % 2 == 0):
    sum -= i
  else:
    sum += i
  if(i == a and sum < 0):
    print("-{0}".format(i), end="")
  elif(i % 2 == 0):
    print("-{0}".format(i), end="")
  else:
    print("+{0}".format(i), end="")
print("= {0}".format(sum))
print(sum)

# 11. 제곱수의 개수 출력하기 2개 이상 15개 이하의 중복되지 않는 99이하의 양의 정수를 입력 받아 제곱수의 개수를 출력하는 프로그램을 작성하세요. 
# 단, 입력이 끝났다는 뜻으로 0을 입력 받되, 0은 개수에 포함시키지 않는다

isInput = True
while(isInput):
  n = list(input().split())
  if(n[-1] == 0 or (len(n) <= 15 and len(n) >= 2)):
    isInput = False
  else:
    print('다시입력해주세요')

sum = 0
for i in n[0:len(n) - 1]:
  if(int(int(i) ** 0.5) ** 2 == int(i)):
    sum += 1
print(sum)
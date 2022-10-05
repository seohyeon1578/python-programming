# 4. 앞으로 읽으나 뒤로 읽으나 똑같은 문장을 회문이라고 한다. 
# 에를 들면, 기러기, 일요일 등... 
# 한 숫자를 입력받아 그 숫자와 그 숫자를 뒤집은 수를 더했을 때 회문이 되면 Yes, 아니면 No를 출력한다.

n = int(input())
r = int(str(n)[::-1])
result = n + r
result = str(result)

isfor = True

for i in range(len(result) // 2):
  if(result[i] != result[-1 -i]):
    isfor = False
    break

if(isfor):
  print('Yes')
else:
  print('No')
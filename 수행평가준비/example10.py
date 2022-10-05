# 10. 50개의 데이터 1, 3, 5, 7......99를 range()함수를 이용하여 튜플에 초기화시킨 후 모든 요소의 합을 구하는 프로그램
temp = tuple(i for i in range(100) if i % 2 != 0)
sum = 0
for i in temp:
  sum += i
print(sum)
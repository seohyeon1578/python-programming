# 5. 카페에서 아메리카노 한 잔을 사면 쿠폰에 도장을 찍어준다. 
# 카페에서 요구하는 도장의 개수를 채우면 아메리카노 한 잔을 다시 교환할 수 있다.
# 그런데 이 가게는특이하게도 쿠폰을 모아 아메리카노로 교환할 때 에도 도장을 또 하나 찍어준다. 
# 내가 가지고 있는 도장의 개수(k)와 카페에서 요구하는 필요 도장의 개수(n)가 입력되면 최대한 마실 수 있는 아메리카노의 개수를 계산하는 프로그램
# ** 입력조건: 1 <= k <= 2000, 1 <= n <= 1000

isInput = True
while(isInput):
  k, n = map(int, input().split(' '))
  if(k >= 1 and k <= 2000 and n >=1 and n <= 1000):
    isInput = False
  else:
    print('다시 입력해주세요.')
    print('입력조건: 1 <= k <= 2000, 1 <= n <= 1000')

cnt = 0
if(n == 1): print('마음껏 먹으세요^^')
else:
  while(k >= n):
    k -= n
    k += 1
    cnt += 1
  print("마실 수 있는 아메리카노 개수: {0}, 남은도장개수: {1}".format(cnt, k))


# 재귀호출 사용
import sys
sys.setrecursionlimit(100)

def func(k, n, cnt):
  if(k >= n):
    k -= n
    k += 1
    cnt += 1
    func(k, n, cnt)
  else: 
    print("마실 수 있는 아메리카노 개수: {0}, 남은도장개수: {1}".format(cnt, k))

r = func(k, n, 0)
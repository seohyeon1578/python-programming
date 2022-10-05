# 9. 세 자리 양의 정수 A, B, C가 주어지면,
# A * B * C 의 계산 결과에서 0부터 9까지의 숫자가 각각 몇 번씩 쓰였는지 구하는 프로그램

temp = {
  0:0,
  1:0,
  2:0,
  3:0,
  4:0,
  5:0,
  6:0,
  7:0,
  8:0,
  9:0
}
A, B, C = map(int, input().split())
result = list(str(A * B * C))
for i in range(10):
  temp[i] = int(result.count(str(i)))
print(temp)
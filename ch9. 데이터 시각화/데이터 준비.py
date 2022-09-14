import csv

f = open(r'C:\Users\DGSW\Documents\GitHub\python-programming\데이터\card.csv', 'r', encoding='UTF-8')   # 파일 오픈
data = csv.reader(f)                                                                                    # 파일 읽기
next(data)                                                                                              # 파일 헤더 건너뛰기
data = list(data)                                                                                       # 파일 리스트로 바꾸기

# 카드이용일자 모두 출력하기
for row in data:
  print(row[0])

# 카드 사용금액 모두 출력하기
for row in data:
  print(row[-3])

# 카드 사용처와 금액 모두 출력하기
for row in data:
  print(row[5], '에서', row[6], '원 사용')

# 카드 사용처와 금액 모두 출력하기
for row in data:
  store = row[5]
  payment = row[6]
  print(store, '에서', payment, '원 사용')
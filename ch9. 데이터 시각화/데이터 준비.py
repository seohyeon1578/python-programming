import matplotlib.pyplot as plt
import csv

f = open(r'C:\Users\DGSW\Documents\GitHub\python-programming\데이터\card.csv', 'r', encoding='UTF-8')   # 파일 오픈
data = csv.reader(f)                                                                                    # 파일 읽기
next(data)                                                                                              # 파일 헤더 건너뛰기
data = list(data)                                                                                       # 파일 리스트로 바꾸기

plt.rc('font', family='Malgun Gothic')

# 카드이용일자 모두 출력하기
# for row in data:
#   print(row[0])

# 카드 사용금액 모두 출력하기
# for row in data:
#   print(row[-3])

# 카드 사용처와 금액 모두 출력하기
# for row in data:
#   print(row[5], '에서', row[6], '원 사용')

# 카드 사용처와 금액 모두 출력하기
# for row in data:
#   store = row[5]
#   payment = row[6]
#   print(store, '에서', payment, '원 사용')

# 이용금액의 합
# sum = 0
# for row in data:
#   sum += int(row[-3])

# print(sum)

# 월별 이용금액의 합 + ver+ ical 막대그래프 그리기
# plt.title('월별 이용금액의 합')
# month = ['Oct', 'Nov', 'Dec']
# sales = [0, 0, 0]
# for row in data:
#   if(row[0].split("-")[1] == "10"):
#     sales[0] += int(row[-3])
#   elif (row[0].split("-")[1] == "11"):
#     sales[1] += int(row[-3])
#   else:
#     sales[2] += int(row[-3])
# print('10월: ', sales[0], '11월: ', sales[1], '12월: ', sales[2])

# plt.bar(month, sales, color="r")

# current_values = plt.gca().get_yticks()
# plt.gca().set_yticklabels(['{:.0f}만'.format(x / 10000) for x in current_values]) 

# 택시비에 사용한 월별 이용금액 + 배달음식 + 꺽은선 그래프
# month = ['Oct', 'Nov', 'Dec']
# taxi = [0, 0, 0]
# food = [0, 0, 0]
# for row in data:
#   if(row[-4].find('택시') != -1):
#     if(row[0].split("-")[1] == "10"):
#       taxi[0] += int(row[-3])
#     elif (row[0].split("-")[1] == "11"):
#       taxi[1] += int(row[-3])
#     else:
#       taxi[2] += int(row[-3])
#   elif(row[-4] == "(주)우아한형제들"):
#     if(row[0].split("-")[1] == "10"):
#       food[0] += int(row[-3])
#     elif (row[0].split("-")[1] == "11"):
#       food[1] += int(row[-3])
#     else:
#       food[2] += int(row[-3])
# plt.title('10-12월 택시비/배달음식비 지출현황')
# plt.plot(month, taxi, color='r', label="택시비")
# plt.plot(month, food, color='b', label="배달음식")
# plt.legend()

plt.show()
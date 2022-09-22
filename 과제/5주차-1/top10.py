# 1. card.csv 파일을 이용하고, 딕셔너리의 Key와 Value를 이용하여 지출액 상위 10개의 가맹점 이름과 해당 가맹점에서 10월부터 12월까지 사용한 이용금액의 합을 구하세요.

import matplotlib.pyplot as plt
import csv

f = open(r'C:\Users\DGSW\Documents\GitHub\python-programming\데이터\card.csv', 'r', encoding='UTF-8')
data = csv.reader(f)                                                                                    
next(data)                                                                                              
data = list(data)

dic = {}

for row in data:
  if row[-1] == '전표매입':
    if dic.get(row[-4]):
      dic[row[-4]] += int(row[-3])
    else:
      dic[row[-4]] = int(row[-3])

result = sorted(dic.items(), key=lambda x: x[1], reverse=True)
result = result[0:10]
print(result)

# 2. 딕셔너리를 이용해서 돈을 많이 쓴 가맹점 10개를 골라 가로형 막대 그래프를 그리세요.

result = [data for i in range(10) for data in result[i]]
name = result[0:20:2]
sales = result[1:20:2]

x = [i * 100000 for i in range(15)]
value = [str(int(i * 100000 / 10000)) + '만원' if i != 0 else '0' for i in range(15)]

plt.rc('font', family='Malgun Gothic')
plt.title('지출액 상위 10')
plt.barh(name, sales, color="r")
plt.xticks(x, value)

plt.show()
# 핫플레이스 인구 분석

from cProfile import label
from turtle import color
import matplotlib.pyplot as plt
import csv

f = open(r'C:\Users\DGSW\Documents\GitHub\python-programming\데이터\LOCAL_PEOPLE_DONG_202208.csv', 'r', encoding='UTF-8')
data = csv.reader(f)
next(data)
data = list(data)

plt.rc('font', family='Malgun Gothic')

dong_code = 11680545
dong2_code = 11110560

# 8월 시간대별 평균인구 꺽은선 그래프그리기
population = [0 for _ in range(24)]
population2 = [0 for _ in range(24)]

for row in data:
  if(int(row[2]) == dong_code):
    time = int(row[1])
    p = float(row[3])
    population[time] += p
  elif(int(row[2]) == dong2_code):
    time = int(row[1])
    p = float(row[3])
    population2[time] += p

for i in range(24):
  population[i] /= 31
  population2[i] /= 31

y = [i * 5000 for i in range(13)]
value = [str(i * 5000 / 10000) + '만명' for i in range(13)]
plt.title('압구정동, 평창동 시간대별 평균인구(비교)')
plt.plot([str(i) for i in range(24)], population, color='b', label='압구정동')
plt.plot([str(i) for i in range(24)], population2, color='r', label='평창동')
plt.xlabel('시간대')
plt.ylabel('평균인구수')
plt.yticks(y, value)
plt.legend()

plt.show()
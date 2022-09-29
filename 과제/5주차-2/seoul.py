# 행정동명  행정동코드   위도       경도
# 압구정동  11680545 37.530734 127.028461
# 혜화동    11110650 37.587817 127.001745
# 평창동    11110560 37.613029 126.974485
# 이태원1동 11170650 37.532612 126.990182
# 한남동    11170685 37.537541 127.005165
# 능동      11215780 37.550578 127.081722
# 성북동    11290525 37.597248 126.992899
# 신사동    11680510 37.523807 127.026492
# 청담동    11680565 37.524399 127.050457
# 삼성1동   11680580 37.514315 127.062824

# 1. 위의 10개 동의 시간대별 총생활인구의 평균을 구하여 꺽은 선 그래프에 10개 동의 그래프를 그립니다.

import matplotlib.pyplot as plt
import csv

f = open(r'C:\Users\DGSW\Documents\GitHub\python-programming\데이터\LOCAL_PEOPLE_DONG_202208.csv', 'r', encoding='UTF-8')
data = csv.reader(f)
next(data)
data = list(data)

dong_code1 = 11680545
dong_code2 = 11110650
dong_code3 = 11110560
dong_code4 = 11170650
dong_code5 = 11170685
dong_code6 = 11215780
dong_code7 = 11290525
dong_code8 = 11680510
dong_code9 = 11680565
dong_code10 = 11680580

for i in range(1, 11):
  globals()['population{}'.format(i)] = [0 for _ in range(24)]

for row in data:
  if(int(row[2]) == dong_code1):
    time = int(row[1])
    p = float(row[3])
    population1[time] += p
  elif(int(row[2]) == dong_code2):
    time = int(row[1])
    p = float(row[3])
    population2[time] += p
  elif(int(row[2]) == dong_code3):
    time = int(row[1])
    p = float(row[3])
    population3[time] += p
  elif(int(row[2]) == dong_code4):
    time = int(row[1])
    p = float(row[3])
    population4[time] += p
  elif(int(row[2]) == dong_code5):
    time = int(row[1])
    p = float(row[3])
    population5[time] += p
  elif(int(row[2]) == dong_code6):
    time = int(row[1])
    p = float(row[3])
    population6[time] += p
  elif(int(row[2]) == dong_code7):
    time = int(row[1])
    p = float(row[3])
    population7[time] += p
  elif(int(row[2]) == dong_code8):
    time = int(row[1])
    p = float(row[3])
    population8[time] += p
  elif(int(row[2]) == dong_code9):
    time = int(row[1])
    p = float(row[3])
    population9[time] += p
  elif(int(row[2]) == dong_code10):
    time = int(row[1])
    p = float(row[3])
    population10[time] += p

y = [i * 250000 for i in range(10)]
value = [str(int(i * 250000 / 10000)) + '만명' for i in range(10)]

plt.rc('font', family='Malgun Gothic')
plt.title("시간대별 총생활인구")
plt.plot([str(i) for i in range(24)], population1, color='black', label='압구정동')
plt.plot([str(i) for i in range(24)], population2, color='pink', label='혜화동')
plt.plot([str(i) for i in range(24)], population3, color='purple', label='평창동')
plt.plot([str(i) for i in range(24)], population4, color='darkblue', label='이태원1동')
plt.plot([str(i) for i in range(24)], population5, color='skyblue', label='한남동')
plt.plot([str(i) for i in range(24)], population6, color='darkgreen', label='능동')
plt.plot([str(i) for i in range(24)], population7, color='lime', label='성북동')
plt.plot([str(i) for i in range(24)], population8, color='darkorange', label='신사동')
plt.plot([str(i) for i in range(24)], population9, color='yellow', label='청담동')
plt.plot([str(i) for i in range(24)], population10, color='red', label='삼성1동')
plt.xlabel('시간대')
plt.ylabel('평균인구수')
plt.yticks(y, value)
plt.legend()
plt.show()

# 2. 위의 정보와 서울시 생활인구 데이터를 이용하여 지도에 결과를 표시합니다.
# 마커를 표시하되, 오후 6시 기준 가장 평균이 높은 동의 경우 아이콘의 색상이 Red, 
# 평균이 높은 쪽에 속할 수록 아이콘의 색상이 Red에 가까운 색으로 표시하고, 
# 가장 평균이 가장 낮은 동의 경우 아이콘 색상이 Blue, 평균이 낮은 쪽에 속할 수록 Blue에 가까운 색으로 표시하도록 합니다.
# 아이콘은 10개 동이 모두 서로 다른 모양이어야 합니다. 
# 마커에 마우스가 올라가면 해당동 이름이 뜨면 됩니다.

import folium

def rgb_to_hex(r, g, b):
  r, g, b = int(r), int(g), int(b)
  return '#' + hex(r)[2:].zfill(2) + hex(g)[2:].zfill(2) + hex(b)[2:].zfill(2)

lat1, long1 = 37.530734, 127.028461
lat2, long2 = 37.587817, 127.001745
lat3, long3 = 37.613029, 126.974485
lat4, long4 = 37.532612, 126.990182
lat5, long5 = 37.537541, 127.005165
lat6, long6 = 37.550578, 127.081722
lat7, long7 = 37.597248, 126.992899
lat8, long8 = 37.523807, 127.026492
lat9, long9 = 37.524399, 127.050457
lat10, long10 = 37.514315, 127.062824

lat = [lat1, lat10, lat8, lat9, lat5, lat2, lat7, lat3, lat6, lat4]
long = [long1, long10, long8, long9, long5, long2, long7, long3, long6, long4]
name = ["압구정동", "삼성1동", "신사동", "청담동", "한남동", "혜화동", "성북동", "평창동", "능동", "이태원1동"]
icon = ["star", "heart", "wifi", "music", "gamepad", "question", "headphones", "camera", "thumbs-up", "shield"]


population = [population1[18], population2[18], population3[18], population4[18], population5[18], population6[18], population7[18], population8[18], population9[18], population10[18]]
population.sort(reverse=True)

color = [rgb_to_hex(255 - (i * 28.4), 0, 0 + (i * 28.4)) for i in range(10)]

map_y = folium.Map([lat5, long5], zoom_start=12)
for i in range(10):
  folium.Marker([lat[i], long[i]], tooltip=name[i], icon=folium.Icon(icon_color=color[i],icon=icon[i], prefix='fa')).add_to(map_y)

map_y
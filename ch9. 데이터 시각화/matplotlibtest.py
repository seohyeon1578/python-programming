import matplotlib.pyplot as plt
import random

# plt.plot([1, 5, 7, 3, 7])

# 제목 넣기
plt.rc('font', family='Malgun Gothic')
plt.title('키와 몸무게의 상관관계')

# month = ["Mar", "Apr", "May", "Jun", "Jul"]
# sales = [1, 5, 7, 3, 7]

# 기본 선
# plt.plot(month, sales, color="r")

# 막대 그래프
# plt.bar(month, sales, color="r")
# 막대 방향 바꾸기
# plt.barh(month, sales, color="r")

# 원 그래프
# labels = ['A형', 'B형', 'O형', 'AB형']
# ratio = [20, 20, 12, 48]
# plt.pie(ratio, labels, autopct='%1.1f%%')

# 빈도
# data = [1, 2, 3, 3, 3, 5, 7, 7, 8, 10]
# plt.hist(data, bins=30)

# 산점도
# kor = [80, 20, 50, 20, 10, 50, 60, 30, 60]
# eng = [90, 40, 60, 40, 10, 30, 50, 70, 90]
# height = [random.randint(100, 200) for i in range(100)]
# weight = [random.randint(20, 100) for i in range(100)]
# score = [random.randint(1, 1000) for i in range(100)]
# plt.scatter(height, 
#             weight,
#             s=score, 
#             c=score, 
#             cmap='RdPu')
# plt.colorbar(label='키')

# Box plot
# plt.boxplot(kor, labels='국어')

# 꺽은선 그래퍼 겹쳐 그리기
# singer = ['A', 'B', 'C', 'D', 'E']
# week1 = [42, 58, 19, 92, 84]
# week2 = [53, 52, 48, 98, 73]
# plt.plot(singer, week1, color='r', label='첫째 주')
# plt.plot(singer, week2, color='b', label='둘째 주')

# 막대 그래프 겹쳐 그리기
# week1 = [-week1[i] for i in range(len(week1))]
# plt.barh(singer, week1, color='pink', label='첫째 주')
# plt.barh(singer, week2, color='b', label='둘째 주')
# plt.rcParams['axes.unicode_minus'] = False

# 산점도 겹쳐 그리기
# height1 = [random.randint(140, 180) for _ in range(100)]
# weight1 = [random.randint(40, 80) for _ in range(100)]
# height2 = [random.randint(160, 200) for _ in range(100)]
# weight2 = [random.randint(50, 100) for _ in range(100)]
# score1 = [random.randint(1, 200) for _ in range(100)]
# score2 = [random.randint(1, 200) for _ in range(100)]
# plt.scatter(height1,
#             weight1,
#             s=score1,
#             c="crimson",
#             alpha=0.7,
#             label="그룹1"
#             )
# plt.scatter(height2,
#             weight2,
#             s=score2,
#             c="indigo",
#             alpha=0.7,
#             label="그룹2"
#             )

# Box plot 겹쳐 그리기
kor = [random.randint(10, 100) for _ in range(100)]
eng = [random.randint(10, 100) for _ in range(100)]
plt.boxplot([kor, eng], labels=['국어', '영어'])

# 크기 바꾸기
# plt.figure(figsize=(가로, 세로))

# 범례 넣기
plt.legend()

# 축 이름 넣기
# plt.xlabel('키')
# plt.ylabel('몸무게')

plt.show()  
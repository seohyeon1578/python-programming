import numpy as np

A = np.arange(1, 10, 2)
print(A)

a = np.linspace(0, 10, 100)
print(a)

# 0 ~ 1사이의 난수 100개 생성
np.random.seed(100)

# seed설정한 것 중에 5개 뽑아오기
np.random.rand(5)

# 5행에 3열짜리 난수
np.random.rand(5, 3)

# 정규 분포 만족하는 난수 5개
np.random.randn(5)

# 4명의 학생의 (국어, 수학, 영어)점수 
score = np.array([[99, 93, 60], [98, 82, 93], [93, 65, 81], [78, 82, 81]])
# 합
score.sum()
# 최소
score.min()
# 최대
score.max()
# 평균
score.mean()
# 표준편차
score.std()
# 분산
score.var()

# 국어 점수 평균 (axis=1 학생 1명당 평균)
score.mean(axis=0)

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
x.transpose()
x.T
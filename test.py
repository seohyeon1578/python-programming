from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
import matplotlib.pyplot as plt

# Data_set = np.loadtxt('./data/ThoraricSurgery3.csv', delimiter=",")
# X = Data_set[:, 0:16]
# y = Data_set[:, 16]

# model = Sequential()
# model.add(Dense(30, input_dim=16, activation='relu'))
# model.add(Dense(1, activation="sigmoid"))

# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# history = model.fit(X, y, epochs=5, batch_size=16)

# 최소 제곱
# x = np.array([2, 4, 6, 8])
# y = np.array([81, 93, 91, 97])

# mx = np.mean(x)
# my = np.mean(y)

# print('x의 평균값: ', mx)
# print('y의 평균값: ', my)

# divisor = sum([(i - mx)**2 for i in x])

# def top(x, mx, y, my):
#   d = 0
#   for i in range(len(x)):
#     d += (x[i] - mx) * (y[i] - my)
#   return d
# dividend = top(x, mx, y, my)

# print('분모: ', divisor)
# print('분자: ', dividend)

# a = dividend / divisor

# # y 절편 b를 구하는 공식
# b = my - (mx*a)

# print('기울기 a = ', a)
# print('y 절편 b = ', b)


# 평균 제곱 오차
# fake_a = 3
# fake_b = 76

# x = np.array([2, 4, 6, 8])
# y = np.array([81, 93, 91, 97])

# def predict(x):
#   return fake_a * x + fake_b

# predict_result = []

# for i in range(len(x)):
#   predict_result.append(predict(x[i]))
#   print('공부시간=%.f, 실제점수=%.f, 예측점수=%.f' % (x[i], y[i], predict(x[i])))

# n = len(x)
# def mse(y, y_pred):
#   return (1/n) * sum((y - y_pred)**2)

# print('평균 제곱 오차: ' + str(mse(y, predict_result)))

# 선형 회귀
# x = np.array([2, 4, 6, 8])
# y = np.array([81, 93, 91, 97])

# plt.scatter(x, y)
# plt.show()

# a = 0
# b = 0

# lr = 0.03

# epochs = 2001

# n = len(x)

# for i in range(epochs):
#   y_pred = a * x + b
#   error = y - y_pred

#   a_diff = (2/n) * sum(-x * (error))
#   b_diff = (2/n) * sum(-(error))

#   a = a - lr * a_diff
#   b = b - lr * b_diff

#   if i % 100 == 0:
#     print('epoch=%.f, 기울기=%.04f, 절편=%.04f' % (i, a, b))

# y_pred = a * x + b

# plt.scatter(x, y)
# plt.plot(x, y_pred, 'r')
# plt.show()

# 다중 선형 회귀
# x1 = np.array([2, 4, 6, 8])
# x2 = np.array([0, 4, 2, 3])
# y = np.array([81, 93, 91, 97])


# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter3D(x1, x2, y)
# plt.show()

# a1 = 0
# a2 = 0
# b = 0

# lr = 0.01

# epochs = 2001

# n = len(x1)

# for i in range(epochs):
#   y_pred = a1 * x1 + a2 * x2 + b
#   error = y - y_pred

#   a1_diff = (2/n) * sum(-x1 * (error))
#   a2_diff = (2/n) * sum(-x2 * (error))
#   b_diff = (2/n) * sum(-(error))

#   a1 = a1 - lr * a1_diff
#   a2 = a2 - lr * a2_diff
#   b = b - lr * b_diff

#   if i % 100 == 0:
#     print('epoch=%.f, 기울기1=%.04f, 기울기2=%.04f, 절편=%.04f' % (i, a1, a2, b))

# print("실제 점수: ", y)
# print("예측 점수: ", y_pred)


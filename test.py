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

# 텐서플로 선형 회귀 모델
# x = np.array([2, 4, 6, 8])
# y = np.array([81, 93, 91, 97])

# model = Sequential()

# model.add(Dense(1, input_dim=1, activation='linear'))
# model.compile(optimizer='sgd', loss='mse')

# model.fit(x, y, epochs=2000)

# plt.scatter(x, y)
# plt.plot(x, model.predict(x), 'r')
# plt.show()

# hour = 7
# prediction = model.predict([hour])
# print("%.f시간을 공부할 경우의 예상 점수는 %.02f점입니다." % (hour, prediction))

# 로지스틱 회귀 모델
# x = np.array([2, 4, 6, 8, 10, 12, 14])
# y = np.array([0, 0, 0, 1, 1, 1, 1])

# model = Sequential()
# model.add(Dense(1, input_dim=1, activation='sigmoid'))

# model.compile(optimizer="sgd", loss="binary_crossentropy")
# model.fit(x, y, epochs=5000)

# plt.scatter(x, y)
# plt.plot(x, model.predict(x), 'r')
# plt.show()

# hour = 7
# prediction = model.predict([hour])
# print("%.f시간을 공부할 경우, 합격 예상 확률은 %.01f%%입니다." % (hour, prediction * 100))

# xor

# w11 = np.array([-2, -2])
# w12 = np.array([2, 2])
# w2 = np.array([1, 1])
# b1 = 3
# b2 = -1
# b3 = -1

# def MLP(x, w, b):
#   y = np.sum(w * x) + b
#   if y <= 0:
#     return 0
#   else:
#     return 1

# def NAND(x1, x2):
#   return MLP(np.array([x1, x2]), w11, b1)

# def OR(x1, x2):
#   return MLP(np.array([x1, x2]), w12, b2)

# def AND(x1, x2):
#   return MLP(np.array([x1, x2]), w2, b3)

# def XOR(x1, x2):
#   return AND(NAND(x1, x2), OR(x1, x2))

# for x in [(0, 0), (1, 0), (0, 1), (1, 1)]:
#   y = XOR(x[0], x[1])
#   print("입력 값: " + str(x) + " 출력 값: " + str(y))
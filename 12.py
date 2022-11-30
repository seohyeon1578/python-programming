import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split, KFold
from sklearn.metrics import accuracy_score
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping

# 다중 분류 문제
# df = pd.read_csv('./data/iris3.csv')

# print(df.head())

# sns.pairplot(df, hue="species")
# plt.show()

# X = df.iloc[:, 0:4]
# y = df.iloc[:, 4]

# print(X[0:5])
# print(y[0:5])

# y = pd.get_dummies(y)

# print(y[0:5])

# model = Sequential()
# model.add(Dense(12, input_dim=4, activation='relu'))
# model.add(Dense(8, activation='relu'))
# model.add(Dense(3, activation='softmax'))
# model.summary()

# model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# history = model.fit(X, y, epochs=50, batch_size=5)

# # 모델 성능 검증
# df = pd.read_csv('./data/sonar3.csv', header=None)

# print(df.head())

# print(df[60].value_counts())

# X = df.iloc[:, 0:60]
# y = df.iloc[:, 60]

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=True)

# model = Sequential()
# model.add(Dense(24, input_dim=60, activation='relu'))
# model.add(Dense(10, activation='relu'))
# model.add(Dense(1, activation='sigmoid'))

# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# history = model.fit(X_train, y_train, epochs=200, batch_size=10)

# score = model.evaluate(X_test, y_test)
# print('Test accuracy:', score[1])

# model.save('./data/model/my_model.hdf5')

# del model

# model = load_model('./data/model/my_model.hdf5')

# score = model.evaluate(X_test, y_test)
# print('Test accuracy:', score[1])

# k = 5
# kfold = KFold(n_splits=k, shuffle=True)
# acc_score = []

# def model_fn():
#   model = Sequential()
#   model.add(Dense(24, input_dim=60, activation='relu'))
#   model.add(Dense(10, activation='relu'))
#   model.add(Dense(1, activation='sigmoid'))
#   return model

# for train_index, test_index in kfold.split(X):
#   X_train, X_test = X.iloc[train_index, :], X.iloc[test_index, :]
#   y_train, y_test = y.iloc[train_index], y.iloc[test_index]
  
#   model = model_fn()
#   model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
#   history = model.fit(X_train, y_train, epochs=200, batch_size=10, verbose=0)

#   accuracy = model.evaluate(X_test, y_test)[1]
#   acc_score.append(accuracy)

# avg_acc_score = sum(acc_score) / k

# print('정확도: ', acc_score)
# print('정확도 평균: ', avg_acc_score)

# 모델 성능 향상

df = pd.read_csv('./data/wine.csv', header=None)

print(df.head())

X = df.iloc[:, 0:12]
y = df.iloc[:, 12]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=True)
model = Sequential()
model.add(Dense(30, input_dim=12, activation='relu'))
model.add(Dense(12, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.summary()

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

early_stopping_callback = EarlyStopping(monitor='val_loss', patience=20)

modelpath = "./data/model/Ch14-4-bestmodel.hdf5"
checkpointer = ModelCheckpoint(filepath=modelpath, verbose=0, monitor='val_loss', save_best_only=True)

history = model.fit(X_train, y_train, epochs=2000, batch_size=500, validation_split=0.25, verbose=1, callbacks=[early_stopping_callback, checkpointer])

# hist_df = pd.DataFrame(history.history)
# print(hist_df)

# y_vloss = hist_df['val_loss']
# y_loss = hist_df['loss']

# x_len = np.arange(len(y_loss))
# plt.plot(x_len, y_vloss, "o", c="red", markersize=2, label="Testset_loss")
# plt.plot(x_len, y_loss, "o", c="b", markersize=2, label="TestTrainset_lossset_loss")

# plt.legend(loc='upper right')
# plt.xlabel('epoch')
# plt.ylabel('loss')
# plt.show()  

score = model.evaluate(X_test, y_test)
print('Test accuracy: ', score[1])

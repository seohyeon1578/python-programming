from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./train.csv')

print(df.head(5))

print(df['Survived'].value_counts())

print(df.describe())

# 전처리
# 성별 숫자로 변환 남성 0, 여성 1
df.Sex[df['Sex'] == 'female'] = 1
df.Sex[df['Sex'] == 'male'] = 0

# 나이에 null값이 있어 평균값으로 대체, cabin 선실은 null값이 너무 많아 배제
print(df.isnull().sum())
df['Age'].fillna(value=df['Age'].mean(), inplace=True)

# 1등석에 탔을 때와 2등석에 탓을 때의 죽은 비율을 보기 위해 탑승등급을 1등급, 2등급, 3등급으로 나눔
dummies = pd.get_dummies(df['Pclass'])
del df['Pclass']
df = pd.concat([df, dummies], axis=1, join='inner')
df.rename(columns= {1: 'ClassOne', 2: 'ClassTwo', 3: 'ClassThree'}, inplace=True)

print(df.head())

print(df.describe())

print(df.corr())

colormap = plt.cm.gist_heat
plt.figure(figsize=(12, 12))
sns.heatmap(df.corr(), linewidths=0.1, vmax=0.5, cmap=colormap, linecolor='white', annot=True)
plt.show()

# Survived와 Fare(운임),ClassOne(1등석)의 상관관계가 높다 (하지만 생각해보았을 때 운임은 생존여부와 관계 X)
plt.hist(x=[df.ClassOne[df['Survived'] == 0], df.ClassOne[df['Survived'] == 1]], bins=30, histtype='barstacked', label=['die', 'live'])
plt.legend()
plt.show()

# 여자, 어린이 1등석이 살아남을 확률이 높을거라 생각해. 성별 나이 1등석 2등석 데이터를 X로 지정
X = df[['Sex', 'Age', 'ClassOne', 'ClassTwo']].astype(float)
y = df.iloc[:,1:2].astype(float)

model = Sequential()
model.add(Dense(12, input_dim=4, activation='relu', name='Dense_1'))
model.add(Dense(8, activation='relu', name='Dense_2'))
model.add(Dense(1, activation='sigmoid', name='Dense_3'))
model.summary()

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# 약 79.57%의 정확도를 보임
history = model.fit(X, y, epochs=100, batch_size=5)
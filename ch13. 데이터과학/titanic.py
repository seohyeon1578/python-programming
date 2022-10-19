import pandas as pd
import os, re

os.chdir(r'C:\Users\DGSW\Documents\GitHub\python-programming\데이터')

df = pd.read_csv('titanic.csv', encoding='cp949')

# PassengerId: 승객의 ID이다.
# Survived: 생존 여부
# Pclass: 탑승 등급을 나타낸다. 클래스 1, 클래스 2, 클래스 3의 3가지 클래스가 있다.
# Name: 승객의 이름.
# Sex: 승객의 성별.
# Age: 승객의 나이.
# SibSp: 승객에게 형제 자매와 배우자가 있음을 나타낸다.
# Parch: 승객이 혼자인지 또는 가족이 있는지 여부.
# Ticket: 승객의 티켓 번호.
# Fare: 운임.
# Cabin : 승객의 선실.
# Embarked: 탑승한 지역.

# print(df.Age)
# print(df['Age'])

# print(df.Age.max())

# print(df.Age.mean())

# 1등실 중 최고령자
# print(df.Age[(df.Pclass == 1) & (df.Survived == 1)].max())

# print(df.describe())
# print(df.dtypes)

# dfi = pd.read_csv('titanic.csv', encoding='cp949', index_col=0)
# dfi.to_excel('titanic_index.elxs', sheet_name='PassengerId')

# print(df.loc[:, ['Name', 'Age', 'Gender']])
# print(df.loc[:, ['Name', 'Age', 'Gender']][(df.Gender == "female") & (df.Survived == 1) & (df.SibSp == 1)])

# print(df[['Age', 'Fare']].median())
# print(df[['Gender', 'Age']].groupby("Gender").mean())
# print(df.groupby(['Gender', 'Pclass'])["Fare"].mean())

print(df.Pclass.value_counts())
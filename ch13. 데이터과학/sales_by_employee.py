import pandas as pd
import os, re

os.chdir(r'C:\Users\DGSW\Documents\GitHub\python-programming\데이터')

df = pd.read_csv('sales_by_employee.csv', encoding='cp949', parse_dates=["Date"])

# print(df.tail())

# Date를 인덱스로 삼은 피벗테이블
# print(df.pivot_table(index="Date"))

# aggfunc의 기본값은 평균(mean) *sum, median, mean등
# print(df.pivot_table(index="Date", aggfunc="sum"))

# values 보여지는 값(보여지길 원하는 컬럼을 넣으면 된다)
# print(df.pivot_table(index="Date", values="Revenue", aggfunc="sum"))

# 컬럼 지정 가능(이름 별로 보고싶다)
# print(df.pivot_table(index="Date", columns="Name", values="Revenue", aggfunc="sum"))

# (fill_value = 0) = NaN값 0으로 바꾸기
# print(df.pivot_table(index="Date", columns="Name", values="Revenue", aggfunc="sum", fill_value=0))

# margins=True, 행과 열에 All이 추가된다
# print(df.pivot_table(index="Date", columns="Name", values="Revenue", aggfunc="sum", fill_value=0, margins=True))

# 몇번 판매 했는지 (개수)
# print(df.pivot_table(index="Date", columns="Name", values="Revenue", aggfunc="count"))

# 합 개수 둘다
# print(df.pivot_table(index="Date", columns="Name", values="Revenue", aggfunc=["sum", "count"], fill_value=0))

# revenue는 합, Expenses는 개수로 각각 지정
# print(df.pivot_table(index="Date", columns="Name", values=["Revenue", "Expenses"], aggfunc={"Revenue":"sum", "Expenses":"count"}, fill_value=0))

# 인덱스 2개
print(df.pivot_table(index=["Name", "Date"], values="Revenue", aggfunc="sum").head(10))
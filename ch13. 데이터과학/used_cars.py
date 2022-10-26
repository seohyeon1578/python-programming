import pandas as pd
import os, re

os.chdir(r'C:\Users\DGSW\Documents\GitHub\python-programming\데이터')

df = pd.read_csv('used_cars.csv')
mini_wage = pd.read_csv('minimum_wage.csv')

# 가격의 합계를 집계, 행 측에서 연료 유형별로 결과를 그룹화
# print(df.pivot_table(index="Fuel", values="Price", aggfunc="sum"))

# 자동차의 개수를 집계, 인덱스 축에서 제조업체별로 결과를 그룹화, 열 축에서 변속기 유형을 그룹화, 행과 열 모두에 대한 소계를 표기
# print(df.pivot_table(index="Manufacturer", values="Price", columns="Transmission", aggfunc="count", margins=True))

# 자동차의 평균 가격을 집계, 인덱스 축에 연도 및 연료 유형별로 그룹화 열 축에 변속기 유형을 그룹화
# print(df.pivot_table(index=["Year", "Fuel"], values="Price", columns=["Transmission"], aggfunc="mean"))

# mini_wage를 넓은 형식에서 좁은 형식으로 변화, 즉, 8개의 연도 열에있는 데이터를 하나의 열로 옮기기
# print(mini_wage.melt(id_vars="State", var_name="Year", value_name="Wage"))
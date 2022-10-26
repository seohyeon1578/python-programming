import pandas as pd
import os, re

os.chdir(r'C:\Users\DGSW\Documents\GitHub\python-programming\데이터')

# Birthday열의 값을 날짜/시간으로 효과적으로 변환 (date 타입 변환)
df = pd.read_csv('nfl.csv', encoding='cp949', parse_dates=["Birthday"])

# 이름을 인덱스로 지정하는 2가지 방법
# df = pd.read_csv('nfl.csv', encoding='cp949', parse_dates=["Birthday"], index_col=["Name"])
df = df.set_index('Name')

# 팀당 선수가 몇명인지
# print(df.Team.value_counts())

# 가장 높은 연봉을 받은 5명의 선수
# print(df.nlargest(5, 'Salary'))

# 팀을 알파벳 순서로 정렬 후 연봉순 내림차순 정렬
# print(df.sort_values(['Team', 'Salary'], ascending=[True, False]))

# New York Jets팀에서 가장 나이가 많은 선수는? 그 선수의 생일은?
df = df.reset_index().set_index(keys = "Team")
print(df.loc['New York Jets'].sort_values('Birthday').head(1))
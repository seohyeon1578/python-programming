import pandas as pd
import os, re

os.chdir(r'C:\Users\DGSW\Documents\GitHub\python-programming\데이터')

df = pd.read_csv('nba.csv', encoding='cp949', parse_dates=['Birthday'])

df = df.sort_values(['Team', 'Name'], ascending=[True, False])

df = df.set_index('Name')

df.columns = ["Team", "Pos", "Bir", "Sal"]

print(df.columns)

# print(df.loc["Aaron Gordon", "Team"])
# print(df.loc["Aaron Gordon", ["Team", "Birthday"]])
# print(df.loc["Aaron Gordon", "Team":"Birthday"])

# iloc = 슬라이싱
# print(df.iloc[400:404])

# loc는 양 끝값 포함
# print(df.sort_index().loc["Aaron Gordon": "Admiral Schofield"])

# 팀은 정방향, 이름은 역순
# print(df.sort_values(['Team', 'Name'], ascending=[True, False]))

# 팀 -> 이름 순으로 정렬
# print(df.sort_values(['Team', 'Name']))

# ascending=False 역순
#print(df.sort_values('Name', ascending=False))

# 숫자값만 출력 (sum, min, max, std, mean가능)
# print(df.sum(numeric_only=True))
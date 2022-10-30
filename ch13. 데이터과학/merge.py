import pandas as pd
import os

os.chdir(r'C:\Users\DGSW\Documents\GitHub\python-programming\데이터')

week_1_sales = pd.read_csv('week_1_sales.csv')
week_2_sales = pd.read_csv('week_2_sales.csv')
foods = pd.read_csv('foods.csv')
customers = pd.read_csv('customers.csv')

# 2주간의 판매 데이터를 하나의 DataFrame으로 결합, week1 DF에 'week1'이라는 키를 할당하고, week2 DF에 'week2'라는 키를 할당
print(pd.concat(objs=[week_1_sales, week_2_sales], keys=['week1', 'week2']))

# 2주동안 매주 식당에서 식사한 고객을 찾으세요
print(week_1_sales.merge(right=week_2_sales, how="inner", on="Customer ID").drop_duplicates(subset=["Customer ID"]))

# 2주동안 매주 식당에서 식사를 하고 같은 음식을 주문한 고객을 찾으세요.
print(week_1_sales.merge(right=week_2_sales, how="inner", on=["Customer ID", "Food ID"]))

# 1주차에만 방문한 고객과 2주차에만 방문한 고객이 누구인지 찾으세요.
outher_join = week_1_sales.merge(right=week_2_sales, how="outer", on="Customer ID", indicator=True)
not_both = outher_join["_merge"] != "both"
print(outher_join[not_both])

# week1 DF의 각 행은 음식을 주문한 고객을 나타낸다. 각 행에 대한 고객의 정보를 customers DF에서 가져오세요.
print(week_1_sales.merge(right=customers, how="left", left_on="Customer ID", right_index=True))
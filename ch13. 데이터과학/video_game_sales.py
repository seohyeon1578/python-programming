import pandas as pd
import os, re

os.chdir(r'C:\Users\DGSW\Documents\GitHub\python-programming\데이터')

df = pd.read_csv('video_game_sales.csv')

# print(df.head())

# NA에 관해서만 피벗 테이블 해제
# print(df.melt(id_vars="Name", value_vars="NA").head())

# 전체 다 해제
regional_sales_columns = ["NA", "EU", "JP", "Other"]
# print(df.melt(id_vars="Name", value_vars=regional_sales_columns))

video_game_sales_by_region = df.melt(
  id_vars="Name",
  value_vars=regional_sales_columns,
  var_name="Region",
  value_name="Sales"
)
print(video_game_sales_by_region.head())
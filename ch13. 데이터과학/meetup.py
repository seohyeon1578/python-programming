import pandas as pd
import os, re

os.chdir(r'C:\Users\DGSW\Documents\GitHub\python-programming\데이터')

groups1 = pd.read_csv('groups1.csv')
groups2 = pd.read_csv('groups2.csv')
categories = pd.read_csv('categories.csv')
cities = pd.read_csv('cities.csv', dtype={ "zip": "string" })

# print(pd.concat(objs=[groups1, groups2], ignore_index=True))
# print(pd.concat(objs=[groups1, groups2], keys=["G1", "G2"]))

groups = pd.concat(objs=[groups1, groups2], ignore_index=True)

# Left Joins
# print(groups.merge(categories, how="left", on="category_id").head())

# Inner Joins
# print(groups.merge(categories, how="inner", on="category_id").head())

# Outer Joins
# print(groups.merge(cities, how="outer", left_on="city_id", right_on="id").head())

# outer_join = groups.merge(cities, how="outer", left_on="city_id", right_on="id", indicator=True)

# in_right_only = outer_join["_merge"] == "right_only"
# print(outer_join[in_right_only].head())
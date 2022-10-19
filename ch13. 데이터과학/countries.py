import pandas as pd
import re, os

os.chdir(r'C:\Users\DGSW\Documents\GitHub\python-programming\데이터')

df = pd.read_csv('countries.csv')

df['density'] = df['population'] / df['area']

df2 = pd.DataFrame({ 
  "code" : ["CA"], 
  "country" : ["Canada"],
  "area" : [9984670], 
  "capital" : ["Ottawa"],
  "population" : [34300000]
})
df = df.append(df2, ignore_index = True)
df.drop(index=2, axis=0, inplace=True)
df.drop(['capital'], axis=1, inplace=True)
print(df)

import pandas as pd
import re, os
from scipy import stats
import statsmodels.formula.api as smf

os.chdir(r'C:\Users\DGSW\Documents\GitHub\python-programming\데이터')

df = pd.read_csv('survey.csv')

print(df)

male = df.income[df.sex=='m']
female = df.income[df.sex=='f']

ttest_result = stats.ttest_ind(male, female)
print(ttest_result)

if ttest_result[1] > .05:
  print('p-value는 95% 수준에서 유의하지 않음')
else:
  print('p-value는 95% 수준에서 유의함')

corr = df.corr()
print(corr)
print(df.corr(method='spearman'))
print(df.income.corr(df.stress))

# 선형 회귀
model = smf.ols(formula='jobSatisfaction~English', data=df)
result = model.fit()
print(result.summary())

# 다중 회귀
model2 = smf.ols(formula='jobSatisfaction~English + stress + income', data=df)
result = model2.fit()
print(result.summary())
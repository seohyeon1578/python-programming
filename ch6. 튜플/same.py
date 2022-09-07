s1 = input('첫 번째 문자열:')
s2 = input('두 번째 문자열:')

list1 = list(set(s1) & set(s2))   #교집합

for i in list1:
  print(i, end=" ")
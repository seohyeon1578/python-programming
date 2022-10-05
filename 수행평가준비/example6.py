# 6. 머리 글자어(acronym)은 NATO(North Atlantic Treaty Oraganization)처럼 각 단어의 첫글자를 모아서 만든 문자열이다. 
# 사용자가 문장을 입력하면 해당되는 머리글자어를 출력하는 프로그램을 작성하여 보자.

s = input().split(' ')
for i in range(len(s)):
  print(s[i][:1].upper(), end="")
  
txt = input('입력 텍스트:')
words = txt.split(' ')
unique = set(words) # 집합으로 만들어 자동으로 중복 제거

print('사용된 단어의 개수',len(unique))
print(unique)
# 7. 단어 카운터 만들기
# --- 입력예시: Create the highest, grandest vision possible for your life, because you become what you believe
# --- 출력예시: (
#       Create: 1
#       because: 1
#       become: 1 ...)

# temp = []
# w = list(input().replace(',', '').split())

# for i in w:
#   if i not in temp:
#     print("{0}: {1}".format(i, w.count(i)))
#     temp.append(i)

temp = {}
w = list(input().replace(',', '').split())

for i in w:
  if i not in temp:
    temp[i] = '{0}'.format(w.count(i))

for key, value in temp.items():
  print('{0}: {1}'.format(key, value))
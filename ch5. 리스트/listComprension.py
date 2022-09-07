# 리스트 압축 
# list = [x for x in range(100) if x % 2 == 0 and x % 3 == 0]
# print(list)

# 전치 행렬
myList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

row = len(myList)
col = len(myList[0])
list2 = [[0 for row in range(row)]for col in range(col)]

for x in range(row):
  for y in range(col):
    list2[y][x] = myList[x][y]


print(myList)
print(list2)
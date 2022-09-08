# 3. 리스트에 동전 던지기의 결과를 저장한 결과가 아래와 같습니다. 가장 길게 앞면이나 뒷면이 연속해서 나왔던 위치를 찾는 코드를 작성하세요. 
# 리스트 내용 : [H, T, H, H, H, T, T, H, T, H, T, T]
# ----------- 실행결과
# [1, 1, 0, 0, 1, 0, 1, 1, 1, 0]
# 최대 연속 길이 : 3

myList = ["H", "T", "H", "H", "H", "T", "T", "H", "T", "H", "T", "T"]

result = [0 if myList[i] == myList[i + 1] else 1 for i in range(len(myList) - 1)]
print(result)

myList = ''.join(myList)
max(map(lambda x: len(x), myList.split('H')))
print("최대 연속 길이: ", max(max(map(lambda x: len(x), myList.split(i))) for i in 'HT'))

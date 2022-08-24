print("=======================")
print("메뉴 1번: 새우 버거")
print("메뉴 2번: 치킨 버거")
print("메뉴 3번: 불고기 버거")
print("=======================")

menu = int(input("메뉴를 선택하세요: "))

if menu == 1:
  print("새우버거")
elif menu == 2:
  print("치킨버거")
elif menu == 3:
  print("불고기버거")
else:
  print('잘못 입력하셨습니다.')
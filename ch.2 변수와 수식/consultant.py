name = input("이름: ")
date = input("생년월일: ")  #051008
number = input("전화번호: ")
age = 22 - int(date[:2])

print(name, "님 나이: ", age, "에 맞는 추천........ 번호:", number)
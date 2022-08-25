name = input("이름은 무엇입니까?: ")
weight = float(input("몸무게를 kg 단위로 입력하세요.: "))
height = int(input("키를 cm 단위로 입력하세요.: "))
height /= 100
bmi = weight / (height ** 2)
if bmi < 18.5: 
    result = "저체중" 
elif bmi  < 25: 
    result = "표준"
elif bmi < 30: 
    result = "과체중"
else: 
    result = "비만"
print("{0}의 BMI는 {1:.2f}이며, 현재 {2}의 상태는 {3}입니다." .format(name, bmi, name, result))
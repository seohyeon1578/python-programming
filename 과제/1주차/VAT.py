food = int(input("음식의 비용을 입력해주세요: "))
tip = int(input("팁 비율을 입력해주세요: "))

while True:
  vat = int(input("부가세 비율(<= 20%)을 입력해주세요: "))
  if vat <= 20:
    break
  else:
    print("부가세 비율은 20%를 초과하면 안됩니다.")

person = int(input("식사비용 나눌 사람의 수를 입력해주세요: "))
total = food + (tip / 100 * food) + (vat / 100 * food)

print("=" * 20)
print(f"음식비용: {food}")
print(f"팁 비율: {tip}%")
print(f"부가세 비율: {vat}%")
print(f"식사비용 나눌 사람의 수: {person}명")
print(f"각자 내야하는 돈: {total / person}")
print(f"총액: {total}")
print("=" * 20)
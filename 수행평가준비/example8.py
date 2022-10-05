# 8. 문자열 안에 있는 문자의 개수, 숫자의 개수, 공백의 개수를 계산하는 프로그램
# 결과는 딕셔너리에 저장하여 출력
# --- 사용함수: isalpha() / isdigit() / isspace()
# --- 입력예시: A picture is worth a thousand words.
# --- 출력예시: {"digits": 0, "spaces": 6, "alphas": 29}

w = input().replace('.', '')
temp = {
  "digits": 0,
  "spaces": w.count(" "),
  "alphas": 0,
}

for i in w.split():
  if(i.isalpha()):
    temp["alphas"] += len(i)
  elif(i.isdigit()):
    temp["digits"] += len(i)

print(temp)
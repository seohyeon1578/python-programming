# 6. "MM/DD/YYYY"형식으로 표기된 날짜를 받아서 "YYYYMMDD" 형태로 출력하는 프로그램을 작성하세요.
# ------- 실행결과
# "05/21/2022" -> "20220521"
# "09/13/2022" -> "20220913"

date = input()

date = date.split("/")
date = date[2] + date[0] + date[1]
print(date)
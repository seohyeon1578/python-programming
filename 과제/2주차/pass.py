import re

def checkPass(p):
  if(len(p) < 8 or not re.search("[a-z]", p) or not re.search("[A-Z]", p) or not re.search("[0-9]", p)):
    print('사용할 수 없는 패스워드입니다. 다시 입력하세요!!')
    return False
  else:
    print('사용 가능한 패스워드 입니다.')
    return True

while True:
  password = input('패스워드를 입력하세요: ')
  if(checkPass(password)):
    break


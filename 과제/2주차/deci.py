def deci2bin(n):
  binaryNum = bin(n)
  return binaryNum[2:]

deci = int(input('10진수: '))
print("2진수: ", deci2bin(deci))

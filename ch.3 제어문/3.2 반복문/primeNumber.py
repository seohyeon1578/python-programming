# list = []
# for i in range(2, 101):
#   isPrime = True
#   for j in range(2, i):
#     if i % j == 0:
#       isPrime = False
#       break
#   if isPrime:
#     list.append(i)
# print(list)



def prime_number(x):
  for i in range(2, x):
    if x % i == 0:
      return False
  return True
  
cnt = 0
x = 1
list = []

while cnt < 50:
  x = x + 1
  if prime_number(x):
    list.append(x)
    cnt = cnt + 1
print(list)



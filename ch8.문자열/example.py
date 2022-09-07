myList = input()

table = {
  "digits": 0,
  "spaces": 0,
  "alphas": 0
}

for i in myList:
  if i.isalpha():
    table["alphas"] += 1
  if i.isdigit():
    table["digits"] += 1
  if i.isspace():
    table["spaces"] += 1
print(table)
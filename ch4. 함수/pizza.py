def get_area(radius):
  return  3.14 * radius ** 2

radius1 = int(input('첫 번째 피자 반지름(cm): '))
radius2 = int(input('두 번째 피자 반지름(cm): '))

print(radius1,'cm 피자 2개의 면적: ', round(get_area(radius1) * 2, 1))
print(radius2,'cm 피자 1개의 면적: ', round(get_area(radius2), 1))

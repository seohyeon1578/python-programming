def weeklyPay(rate, hour):
  if hour > 30:
    return rate * 30 + rate * 1.5 * (hour - 30)
  else:
    return rate * hour

rate = int(input('시급을 입력하시오: '))
hour = int(input('근무 시간을 입력하시오: '))
print('주급은', weeklyPay(rate,hour))
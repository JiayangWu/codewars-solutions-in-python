#https://www.codewars.com/kata/56548dad6dae7b8756000037
def what_is_the_time(time_in_mirror):
    hour = int(time_in_mirror[0:2])
    minute = int(time_in_mirror[3:5])

    if hour < 11:
      hour1 = 11 - hour
    else:
      hour1 = 23 - hour

    minute1 = 60 - minute
    if minute1 == 60:
      minute1 -=60
      hour1 += 1
    if hour1 > 12:
      hour1 -=12
    ans = ""
    if hour1 > 9 :
      ans = str(hour1) + ':'
    else:
      ans = '0' + str(hour1) + ':'

    if minute1 > 9:
      ans += str(minute1)
    else:
      ans += '0' + str(minute1)
    return ans

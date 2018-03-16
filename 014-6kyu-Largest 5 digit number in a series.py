#https://www.codewars.com/kata/51675d17e0c1bed195000001
def solution(digits):
    l = len(digits)
    digits = str(digits)
    start = 0
    end = 5
    max = 0
    while 1:
      temp = digits[start:end]
      if int(temp) > max:
        max = int(temp)
      start += 1
      end +=1
      if end == l +1:
        break
    return max

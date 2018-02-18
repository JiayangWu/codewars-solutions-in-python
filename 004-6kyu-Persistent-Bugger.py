#https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec
def persistence(n):
    # your code
  s = 0
  i = 1
  temp = 1
  t = 1
  while n > 9:
    temp = str (n)
    for j in range(len(temp)):
      t *= int(temp[j])
    s += 1
    n = t
    t = 1
  return s

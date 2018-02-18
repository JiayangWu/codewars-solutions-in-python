# https://www.codewars.com/kata/541c8630095125aba6000c00
def digital_root(n):
  i = 1
  temp = 1
  t = 0
  while n > 9:
    t = 0
    temp = str (n)
    for j in range(len(temp)):
      t += int(temp[j])
    n = t
  return t

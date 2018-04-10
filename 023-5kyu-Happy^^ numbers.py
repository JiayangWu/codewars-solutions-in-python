def is_happy(n):
    for i in range(100):
      k = check(n)
      if k == 1:
        return True
      else:
        n = k
    return False
def check(n):
  sum = 0
  while ( n > 9 ):
    sum += (n % 10) ** 2
    n = n - n % 10
    n /= 10
  return sum + n ** 2

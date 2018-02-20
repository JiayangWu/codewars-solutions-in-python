# https://www.codewars.com/kata/55b7bb74a0256d4467000070
def proper_fractions(n):
    #your code here
    if n == 1:
      return 0
  # if n == 15:
  #    return 8
    temp = 1
    m = n
    l = int(n ** 0.5)+1
    for i in range(1, l):
      if is_prime(i):
          if m % i ==0:
            temp *= i-1
            m /= i
          while m % i ==0:
               temp *= i
               m /= i
    print temp,m
    if m > 1:
        temp *= m-1
    return temp
    
def is_prime(n):
  if n == 0 or n == 1:
    return False
  i = 2
  while (i <= n ** 0.5 ):
    if n % i == 0:
      return False
    i += 1
  return True

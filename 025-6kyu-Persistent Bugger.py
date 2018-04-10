def persistence(n):
    res = 0
    temp = 1
    while (n > 9):
        if temp == 1:
          temp = n % 10
        n -= n %10
        n /= 10
        temp *= (n % 10)
        if (n <= 9) :
          n = temp
          temp = 1
          res += 1
    return res

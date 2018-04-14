def is_ore(n):
    temp = 0.0
    divisor = []
    count = 0
    for i in range(1,int(n ** 0.5) + 1):
      if n % i == 0:
        if i ** 2 != n:
          divisor.append(i)
          divisor.append(n / i)
          count += 2
        else:
          divisor.append(i)
          count += 1
    for i in divisor:
      temp += 1.0 / i
      print i,temp,count, 48/3.2
    return (count / temp) - int( count / temp) < 1e-5

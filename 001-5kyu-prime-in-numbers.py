# https://www.codewars.com/kata/54d512e62a5e54c96200019e

def primeFactors(n):

    i = 2
    res = {}
    while n/i != 1:
      if n%i == 0:
        if i in res:
            res[i] = res[i]+1
        else:
            res[i] = 1
        n = n/i
      else:
        i+=1

    if i in res:
        res[i] = res[i]+1
    else:
        res[i] = 1
    t = ''
    res = sorted(res.items(),key = lambda a:a[0])

    for key in res:
        if key[1] == 1:
           t = t + '('+str(key[0]) +')'
        else:
           t = t + '(' +str(key[0]) + '**' + str(key[1]) + ')'
    return t

def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    # your code here
    res = []
    for i in range(a, b + 1):
        if i == getSpecialSum(i):
            res.append(i)
    return res

def getSpecialSum(n):
    digits = [int(d) for d in str(n)]
    res = 0
    for i, d in enumerate(digits):
        res += d ** (i + 1)
    return res
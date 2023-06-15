def order_weight(string):
    res = []
    for num in string.split():
        res.append([num, getWeight(num)])
    res.sort(key = lambda x: (x[1], x))
    return " ".join([num for num, w in res])
    
def getWeight(num):
    num = int(num)
    s = 0
    while num:
        num, m = divmod(num, 10)
        s += m
    return s
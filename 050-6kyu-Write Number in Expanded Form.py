def expanded_form(num):
    res = []
    cnt = 0
    while num:
        num, m = divmod(num, 10)
        if m:
            res.append(m * (10 ** cnt))
        cnt += 1
    return " + ".join([str(x) for x in res[::-1]])
def next_bigger(n):
    s = str(n)
    if check(s):
        return -1
    l = len(s)
    ss = []
    for item in s:
        ss.append(int(item))
    index = l-1
    while(index > 0):
        if int(ss[index-1]) < int(ss[index]):
            for j in range(l-1,index-1,-1):
                print ss[j], ss[index-1]
                if ss[j] > ss[index-1]:
                    print ss[j],ss[index-1],ss
                    temp = ss[j]
                    ss[j] = ss[index-1]
                    ss[index-1] = temp
                    print ss,index,ss[index:]
                    ss = ss[:index] + ss[index:][::-1]
                    break
            break
        else:
            index -=1
    print ss
    res = 0
    for i in range(0,l):
        res += 10 ** i * ss[-(i+1)]
    print res
    return res
def check(s):
    l = len(s)
    index = l-1
    while(index > 0):
      if int(s[index]) >  int(s[index-1]):
          return False
      index -=1
    return True

next_bigger(5)

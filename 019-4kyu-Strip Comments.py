def solution(string,markers):
    #your code here
    c = '\xc2' # for solving special unknown bugs
    print c
    print string, markers
    res = ""
    s = string.split('\n')
    for i in s:
    #  print i
      position = -1
      for j in range(len(i)):
        print i[j]
        if i[j] in markers:
          print i[j],i
          position = j
          break
        if i[j] == c:
          print i[j],i
          position = j
          break
      if position != -1:
        i = i[0:position]
      res += i.rstrip() + "\n"
    return res[0:-1]

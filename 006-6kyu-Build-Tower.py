# https://www.codewars.com/kata/576757b1df89ecf5bd00073b
def tower_builder(n_floors):
    # build here
    res = []
    temp = ''
    for i in range(n_floors):
      temp = ''
      for t in range(n_floors-i-1):
        temp += ' '
      print temp
      for j in range(2*i+1):
        temp += '*'
      print temp
      for k in range(n_floors-i-1):
        temp += ' '
      res.append(temp)
    print res
    return res

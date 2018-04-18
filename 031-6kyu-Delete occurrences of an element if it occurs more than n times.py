def delete_nth(order,max_e):
    temp = {}
    res = []
    for i in order:
      if i not in temp :
        temp[i] = 0
      else:
        temp[i] += 1
      if temp[i] <max_e:
        res.append(i)
    return res

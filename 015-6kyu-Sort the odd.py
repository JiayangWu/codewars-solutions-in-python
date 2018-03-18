def sort_array(s):
    if len(s) == 0:
      return s
    odd = []
    for i in range(len(s)):
      if s[i] % 2 == 1:
        odd.append(s[i])
        s[i] = -999
    odd.sort()
    k = 0
    for i in range(len(s)):
      if s[i] == -999:
        s[i] = odd[k]
        k += 1

    return s

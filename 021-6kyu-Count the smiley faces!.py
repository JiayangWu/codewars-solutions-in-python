def count_smileys(arr):
    res = 0
    for i in arr:
      if check(i):
        res += 1
    return res#the number of valid smiley faces in array/list
def check(i):
    if i[0] != ':' and i[0] != ';':
      return False
    if len(i) == 3 and i[1] != '-' and i[1] != '~':
      return False
    if len(i) == 3 and i[2] != ')' and i[2] != 'D':
      return False
    if len(i) == 2 and i[1] != ')' and i[1] != 'D':
      return False
    return True

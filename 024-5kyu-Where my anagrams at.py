def anagrams(s, words):
    res = []
    s = "".join((lambda x:(x.sort(),x)[1])(list(s)))
    for w in words:
      t = sorted(list(w))
      temp = "".join(x for x in t)
      if temp == s:
        res.append(w)
    return res

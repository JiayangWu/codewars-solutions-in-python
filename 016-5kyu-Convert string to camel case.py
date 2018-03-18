sp = ['-','_']
def to_camel_case(text):
    if len(text) == 0:
      return text
    text = text.replace("_","-")
    s = text.split("-")
    for i in range(len(s)):
      if i == 0:
        continue
      else:
        s[i] = s[i].capitalize()
    res = "".join(i for i in s)
    return res

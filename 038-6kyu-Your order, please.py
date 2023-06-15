def order(sentence):
  dict = {}
  list = []
  sentence_split = sentence.split(" ")
  
  for item in sentence_split:
      for char in item:
          a_code = ord(char)
          if a_code >= ord("0") and a_code <= ord("9"): 
              dict[char] = sentence_split.index(item)
              list.append(a_code - ord("0"))
              break
  list.sort()

  res = []
  for i in list:
       res.append(sentence_split[dict[str(i)]])
          
  return " ".join(item for item in res)

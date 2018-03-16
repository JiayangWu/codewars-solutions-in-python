#https://www.codewars.com/kata/5aa7a581fd8c06b552000177
import random
import numpy as np
def love_language(partner, weeks):
    # your code here
    records = [0, 0, 0, 0, 0]
    print (LOVE_LANGUAGES)
    for i in range( 7 * weeks):
      ran = np.random.randint(0,4)
      respons = partner.response(LOVE_LANGUAGES[ran])
      if 'positive' == respons:
        records[ran] += 1
      else:
        records[ran] -= 1
    print (records)
    return LOVE_LANGUAGES[records.index(max(records))]
      

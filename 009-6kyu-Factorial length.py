#https://www.codewars.com/kata/factorial-length/python
import math
def count(n):
    return int(math.ceil(math.log(2 * math.pi * n, 10) / 2 + n * math.log(n / math.e, 10)))

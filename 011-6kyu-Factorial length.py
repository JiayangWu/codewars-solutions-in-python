#https://www.codewars.com/kata/59f34ec5a01431ab7600005a
import math
def count(n):
    return int(math.ceil(math.log(2 * math.pi * n, 10) / 2 + n * math.log(n / math.e, 10)))

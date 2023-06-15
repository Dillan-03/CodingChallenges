# # Summation of primes < 2,000,000

import math
from Functions import timeThis

def isprime(n):
    if n == 1: return False

    sr = math.sqrt(n)

    for i in range(2, int(sr) + 1):
        # print(i)
        if n % i == 0:
            return False
    return True

@timeThis
def total(x):
    y = 0 
    for i in range(x):
        if isprime(i):
            y += i
    return y


print(total(2000000))

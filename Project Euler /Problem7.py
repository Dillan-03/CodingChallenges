# 10001st prime number

import sys
import math

from Functions import timeThis


@timeThis
def isPrime():
    primes = []
    for iterator in range(0,110000):
        if iterator > 1:
            for i in range(2,iterator):
                if iterator % i == 0:
                    break
            else:
                primes.append(iterator)
                    
    # print(primes)
    print(primes[10001])
    # print(len(primes))
isPrime()   
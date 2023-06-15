# Highly Divsible Triangular Number

import math
from Functions import timeThis



def factors(n):
    factor = []
    for i in range(1,n+1):
        if n % i == 0:
            factor.append(i)

    if len(factor) > 500:
        print(factor,"found it")

        exit()
    # else:
        # return factor

def triangular(x):
    sum = 0
    for i in range(0,x+1):
        sum += i
    return sum

# @timeThis
def compute(y):
    for i in range(1,y+1):
        total = triangular(i)
    print(total,":",factors(total))
        # print(factors(total))

if __name__ == '__main__':
    # compute(10)
    count = 1
    # val = True
    while count < 1000000 :
        compute(count)
        count += 1

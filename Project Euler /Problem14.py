# Longest Collatz sequence


import math
from Functions import timeThis


def even(x):
    return int(x/2)

def odd(x):
    
    return (3*x)+1

 
def check(x):
    holder = []
    while x >= 1:
        if x == 1:
            holder.append(x)
            
            break
        if x % 2 == 0:  
            holder.append(x)
            x = even(x) 
        else:
            holder.append(x)
            x = odd(x)

    print(holder)

          


if __name__ == '__main__':
    check(100)
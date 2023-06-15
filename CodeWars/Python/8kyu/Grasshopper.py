# Grasshopper - Summation 
def summation(num):
    total = 0
    for each_num in range(1,num+1):
        total += each_num
    return total
    

print(summation(100))

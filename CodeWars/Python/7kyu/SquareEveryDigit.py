def square_digits(num):
    num = [int(x) for x in str(num)]
    holder = ''
    for number in range(0,len(num)):
        num[number] = num[number] * num[number]
        holder = holder + str(num[number])
    
    return int(holder)
    
print(square_digits(9119))
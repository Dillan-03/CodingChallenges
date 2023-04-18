def wrap(string, max_width):
    holder = ''
    for i in range(0,len(list(string)),max_width):
        holder = holder + (string[i:i+max_width]) + '\n'

    return holder[0:-1]


print(wrap('bscnksbcjscksbcjksbckjdscsbdcbsdkjbcsdjcbsdjkcbsdkjbckjd',15))
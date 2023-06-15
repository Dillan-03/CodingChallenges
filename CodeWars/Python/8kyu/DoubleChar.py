def double_char(s):
    holder = []
    for i in range(0,len(list(s))):
        holder.append(s[i])
        holder.append(s[i])

    return ''.join(holder)
    
print(double_char("String"))

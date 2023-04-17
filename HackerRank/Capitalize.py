import sys
def solve(s):
    s = s.split(' ')

    holder = []
    
    for i in s:
        holder.append(i.capitalize())


    return (' '.join(holder))

solve('42w ab')

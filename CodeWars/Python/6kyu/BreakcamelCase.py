def solution(s):
    holder = []
    for i in s:
        if i == i.lower():
            holder.append(i)
        else:
            holder.append(" ")
            holder.append(i)
    
    return "".join(holder)


print(solution("helloWorld"))

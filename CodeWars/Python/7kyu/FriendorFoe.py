def friend(x):
    holder = []
    for friend in range(0,len(x)):
        if (len(list(x[friend])) == 4):
           holder.append(x[friend])

    return holder

print(friend(["Ryan", "Kieran", "Mark",]))
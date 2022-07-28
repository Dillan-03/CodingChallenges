N = int(input())


print(N)
holder= []
for i in range(0,N):
    command = str(input())
    command = command.split()
    if (command[0] == "insert"):
        i = int(command[1])
        e = int(command[2])
        holder.insert(i,e)
    elif (command[0] == "print"):
        print(holder)
    elif (command[0] == "remove"):
        holder.remove(int(command[1]))
    elif (command[0] == "append"):
        holder.append(int(command[1]))
    elif (command[0] == "sort"):
        holder.sort()
    elif (command[0] == "pop"):
        holder.pop()
    elif (command[0] == "reverse"):
        holder.reverse()


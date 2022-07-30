
n = int(input())
arr = map(int, input().split())

# print(list(arr))
holder = (list(arr))

print(holder.sort())
# print(holder)
holder = tuple(set(holder))


print(holder)

print(holder[-2])
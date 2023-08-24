setA = int(input())
nums = str(input())
setB = int(input())
numB = str(input())


nums = set(list(map(int, list(nums.split()))))


numB = set(list(map(int, (list(numB.split())))))

x = (list(nums.difference(numB).union(numB.difference(nums))))
x.sort()
print(x)
for i in (x):
    print(i)

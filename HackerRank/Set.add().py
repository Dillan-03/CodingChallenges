amount = int(input())
s = set()
for i in range(0, amount):
    country = str(input())
    s.add(country)
print(len(s))

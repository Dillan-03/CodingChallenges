def sum_mix(arr):
    for x in range(0,len(arr)):
       arr[x] = int(arr[x])
    return sum(arr)

print(sum_mix([9, 3, '7', '3']))
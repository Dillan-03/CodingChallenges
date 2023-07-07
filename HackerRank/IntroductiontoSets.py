def average(array):
    # your code goes here
    # print(sum(set(array)))
    # print((sum((array))÷/10))
    l = len(set(array))
    s = sum(set(array))
    # print(sum(s÷÷et(array))/l)
    print(l, s, s/l)
    return s/l

    # return (sum([int(i) for i in list((set((array()))))])/int(len([int(i) for i in list((set((array))))])))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

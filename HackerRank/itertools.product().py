from itertools import product

if __name__ == '__main__':
    for i in range(1):
        arrOne = list(map(int, input().split()))
        arrTwo = list(map(int, input().split()))

    for x in arrOne:
        for y in arrTwo:
            print((x, y), end=" ")

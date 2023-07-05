from collections import Counter


if __name__ == '__main__':
    number_of_shoes = int(input())
    shoe_sizes = Counter(map(int, input().split()))
    num_of_customers = int(input())
    total = 0
    for x in range(num_of_customers):
        desired_shoeSize = list(map(int, input().split()))
        if desired_shoeSize[0] in shoe_sizes:
            total += desired_shoeSize[1]
            shoe_sizes[desired_shoeSize[0]] -= 1
            if shoe_sizes[desired_shoeSize[0]] == 0:
                del shoe_sizes[desired_shoeSize[0]]

    print(total)

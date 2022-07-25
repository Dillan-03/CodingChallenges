def high_and_low(numbers):
    numbers = [int(x) for x in numbers.split()]
    numbers.sort()
    return "{} {}".format(numbers[-1],numbers[0])


print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
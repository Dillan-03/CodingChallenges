from numpy import number


def square_sum(numbers):
    for i in range(0,len(numbers)):
        numbers[i] = numbers[i] * numbers[i]
    return sum(numbers)
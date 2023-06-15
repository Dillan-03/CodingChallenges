def remove_smallest(numbers):
    # raise NotImplementedError("TODO: remove_smallest")

    # empty list
    if len(numbers) == 0: return numbers

    # remove smallest value in list
    x = min(numbers)
    numbers.remove(min(numbers))

    return numbers


print(remove_smallest([326, 85, 315, 399, 154, 133]))
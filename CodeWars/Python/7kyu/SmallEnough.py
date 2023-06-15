def small_enough(array, limit):
    for i in range(0,len(array)):
        if array[i] > limit:
            return False

    return True
# Find unique Number
def find_uniq(arr):

    element_count = {}
    
    # Count the occurrences of each element
    for element in arr:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1

    # Find the first element with a count of 1
    for element in arr:
        if element_count[element] == 1:
            return element



print(find_uniq([1, 1, 1, 2, 1, 1]))

def count_substring(string, sub_string):

    count = 0

    for i in range(0, len(string)):
        x  = string[i:i+len(sub_string)]
        if x == sub_string:
            count += 1
    print(count)


print(count_substring('ABCDCDC','CDC'))
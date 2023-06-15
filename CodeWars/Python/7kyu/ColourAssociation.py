def colour_association(arr):
    holder = []
    for row in arr:
        dict = {}
        dict[row[0]] = row[1]
        holder.append(dict)
    return holder


print(colour_association([["white", "goodness"], ["blue", "tranquility"]]))
def points(games):
    total =  0
    for i in games:
        l = list(i)
      
        if (l[int(0)]) > (l[int(-1)]):
            total += 3
        elif (l[int(0)]) < (l[int(-1)]):
            total += 0
        elif (l[int(0)]) == (l[int(-1)]):
            total += 1

        

    return total


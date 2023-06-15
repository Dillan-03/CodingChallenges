def remove_every_other(my_list):
    new = []
    for i in range(0,len(my_list),2):
        new.append(my_list[i])

    my_list = new
    print(new)
    
remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
                #    [1, 3, 5, 7, 9])
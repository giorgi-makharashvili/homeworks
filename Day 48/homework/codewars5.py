def remove_every_other(my_list):
    list1 = []
    for i in range(len(my_list)):
        if i % 2 == 0:
            list1.append(my_list[i])
    return list1
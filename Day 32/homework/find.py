def manual_find(x,y):
    s = 0
    for i in x:
        if y == i:
            return s
        else:
            s +=1
    return -1
def manual_replace(x,y,z):
    res = ""
    for i in x:
        if x == y:
            res += z
        else:
            res += i 
    return res

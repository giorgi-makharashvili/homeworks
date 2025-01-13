def points(games):
    res = 0
    
    for i in games:
        if int(i[0]) > int(i[-1]):
            res +=3
        elif int(i[0]) == int(i[-1]):
            res += 1
            
    return res
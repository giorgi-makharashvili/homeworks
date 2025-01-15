def accum(st):
    listn = []
    
    for i in range(len(st)):
        listn.append((st[i] * (i+1)).capitalize())
    
    return "-".join(listn)
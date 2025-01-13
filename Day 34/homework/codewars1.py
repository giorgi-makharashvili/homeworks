def fake_bin(x):
    res = ""
    
    for i in x:
        if int(i)<5:
            res += "0"
        else:
            res +="1"
    
    return res
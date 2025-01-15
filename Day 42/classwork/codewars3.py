def to_jaden_case(string):
    res = []
    
    for i in string.split():
        res.append(i.capitalize())

    return " ".join(res)
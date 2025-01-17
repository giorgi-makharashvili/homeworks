def open_or_senior(data):
    listn = []
    
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            listn.append("Senior")
        else:
            listn.append("Open")
    return listn
def is_isogram(string):
    string = "".join(sorted(string.lower()))
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return False
    return True
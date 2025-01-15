def xo(s):
    s = s.lower()
    if s == "":
        return True
    
    for i in s:
        if s.count("x") == s.count("o"):
            return True
    return False
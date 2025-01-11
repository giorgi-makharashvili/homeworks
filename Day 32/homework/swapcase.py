def manual_swapcase(s):
    res = ""

    for i in s:
        if i.islower():
            res = res + i.upper()
        else:
            res = res + i.lower()
    return res
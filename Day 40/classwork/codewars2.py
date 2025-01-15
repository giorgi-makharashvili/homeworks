def disemvowel(string_):
    fixed = ""
    for i in string_:
        if i in "aeiou":
            string_.replace(i,"")
        elif i in "AEIOU":
            string_.replace(i,"")
        else:
            fixed +=i
    return fixed
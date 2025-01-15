def find_short(s):
    list1 = [len(i) for i in s.split(" ")]
    return min(list1)
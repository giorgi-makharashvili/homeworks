def descending_order(num):
    num = str(num)
    return int("".join(sorted(num, reverse=True)))
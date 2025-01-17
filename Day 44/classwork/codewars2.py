def maskify(cc):
    cc = list(cc)
    length = len(cc)
    if length > 4:
        last = "".join(cc[-4:])
        return "#" * (length - 4) + str(last)
    else:
        return "".join(cc)
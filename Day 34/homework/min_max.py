def manual_min(lst):
    if not lst:
        return []
    min_value = lst[0]
    for i in lst:
        if i < min_value:
            min_value = i
    return min_value


def manual_max(lst1):
    if not lst1:
        return []
    max_value = lst1[0]
    for i in lst1:
        if i > max_value:
            max_value = i
    return max_value


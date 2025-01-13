def count_positives_sum_negatives(arr):
    list1 = []
    list2 =[]
    
    if arr == []:
        return []
    
    for i in arr:
        if i > 0:
            list1.append(i)
        elif i < 0:
            list2.append(i)
    return [len(list1), sum(list2)]
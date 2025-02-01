def str_count(strng, letter):
    count = 0
    for i in strng:
        if letter == i:
            count += 1
    return count
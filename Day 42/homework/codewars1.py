def solution(text, ending):
    if ending in text and text[-1] in ending:
        return True
    else:
        return False
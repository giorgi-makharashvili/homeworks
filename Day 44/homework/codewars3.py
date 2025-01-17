def find_next_square(sq):
    sq = sq**0.5
    sq = sq+1
    sq = sq*sq
    
    if str(sq)[-2:] != ".0":
        return -1
    else:
        return sq
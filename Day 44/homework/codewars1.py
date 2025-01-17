def longest(a1, a2):
    both = set(a1 + a2)
    done = "".join(sorted(both))
    return done
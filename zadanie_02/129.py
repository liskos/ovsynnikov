for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            f = (a and b) or (c and(not a or b))
            if not f:
                print(b, c, a, int(f))
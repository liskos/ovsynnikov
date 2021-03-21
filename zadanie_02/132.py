for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            f = not(not a or b) or (not a and c)
            if not f:
                print(a,c,b, int(f))
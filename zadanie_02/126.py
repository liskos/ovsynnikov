for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            f = (a or not c) and (not a or b or c)
            if not f:
                print(c, b, a, int(f))
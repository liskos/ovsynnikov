for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            f = (not a or b) and (not( a and b) or  not c)
            if not f:
                print(c,b,a, int(f))
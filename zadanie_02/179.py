for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            f = not (not x or not z) or (x == y)
            if not f:
                print(z, x, y, int(f))

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            f = not(x or y) or (y == z)
            if not f:
                print(y, x, z, int(f))


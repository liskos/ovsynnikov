for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            f = (not(y or z ) or x) or (x == z)
            if not f:
                print(y, z, x, int(f))

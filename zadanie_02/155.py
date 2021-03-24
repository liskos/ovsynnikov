for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            f = (x or not z) and (y or x)
            if f:
                print(y, x, z, int(f))
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            f = (not x or z) and (not x or not y or not z)
            if not f:
                print(y, x, z, int(f))
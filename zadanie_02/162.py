for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            f = (not x or y or z) and (not x or not z)
            if not f:
                print(y, z, x, int(f))
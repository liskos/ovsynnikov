for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            f = (x or not y or not z) and (x or not y or z) and (x or y or z)
            if not f:
                print(y, x, z, int(f))
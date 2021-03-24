for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            f = (x or y or not z) and (not x or y or not z) and (not x or not y or z)
            if f:
                print(y, x, z, int(f))
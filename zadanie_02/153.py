for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            f = (not x or not z) and (not y or  x)
            if  f:
                print(y, z, x, int(f))
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            f = (not x or y) and (not y or z)
            if  f:
                print(z, x, y, int(f))
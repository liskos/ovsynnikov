for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0,1:
                f = (not x or y or z) and (x or not z or not w)
                if not f:
                    print(x, w, z, y,  int(f))
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0,1:
                f = x or (not y or z or w) and (y or not w)
                if not f:
                    print(y, w, z, x,  int(f))
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0,1:
                f = not w or (x or not z) and (not x or not y or z)
                if not f:
                    print(z, w, y, x,  int(f))
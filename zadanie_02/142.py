for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = not x and y and z or x and not y and not w
                if f:
                    print(y, w, z, x,  int(f))
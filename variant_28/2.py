for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = (not y or x or z) and (not z or y)
                if not f:
                    print(z,w,y,x, int(f))
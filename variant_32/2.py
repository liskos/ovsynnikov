for x in 0,1:
    for y in 0,1:
        for w in 0,1:
            for z in 0,1:
                f = (not x or y) or not(not w or z)
                if not f:
                    print(z,y,w,x, int(f))
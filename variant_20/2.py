for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = ((not x or z ) and (not z or w)) or (y ==(x or z))
                if not f:
                    print(y,z,w,x, int(f))
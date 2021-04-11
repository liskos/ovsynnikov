for x in 0,1:
    for y in 0, 1:
        for w in 0, 1:
            for z in 0, 1:
                f = (x and y and not z and w) or (not x and not y and not z and w) or (x and not y and not z and w)
                if f:
                    print(x,w,z,y, int(f))

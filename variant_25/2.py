for x in 0,1:
    for y in 0, 1:
        for w in 0, 1:
            for z in 0, 1:
                f = (x and y and not z and w) or (not w and y and not z and not w) or (x and y and not z and not w)
                if f:
                    print(y,z,w,x, int(f))

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            f = (not x != y or not z)
            if  f:
                print(y,x,z, int(f))
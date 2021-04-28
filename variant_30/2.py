for w in 0,1:
    for x in 0,1:
        for y in 0,1:
            for z in 0,1:
                f = (x and y and not z and not w) or (x and y and z and not w) or (x and not y and not z and not w)
                if f:
                    print(z,y,x,w, int(f))
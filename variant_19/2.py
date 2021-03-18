for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = (not x and not y) or (x == z) or not w
                print(x, y, z, w, "|", int(f))
print("---------------")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = (not x and not y) or (x == z) or not w
                if f:
                    print(x, w, z, y, "|", int(f))
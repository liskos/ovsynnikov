def func(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            f = not(x and a) or (x and 36 ==not 0 or x and 6)
            if not f:
                return False
    return True

for a in range(1, 1000):
    if func(a):
        print(a)
        break
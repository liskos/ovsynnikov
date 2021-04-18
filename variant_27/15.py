def func(a):
    for x in range(0, 1000):
        f = (x & 57 != 0) and (x & 38 != 0) or (x & 9 == 0) or (x & a == 0)
        if not f:
            return False
    return True


for a in range(1, 100):
    if func(a):
        print(a)
        break
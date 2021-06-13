def f(a):
    for x in range(0, 1000):
        ff = x & 51 == 0 or (not (x & 41 == 0) or x & a != 0)
        if not ff:
            return False
    return True



for a in range(0, 1000):
    if f(a):
        print(a)
        break

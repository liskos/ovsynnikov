def func(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            f = (6*x+4*y != 34) or (a > 5*x+3*y)and (a>4*y+15*x-35)
            if not f:
                return False
    return True

for a in range(1, 1000):
    if func(a):
        print(a)
        break
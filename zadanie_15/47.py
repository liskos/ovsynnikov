def func(a):
    p = list(range(10, 20+1))
    q = list(range(12, 15+1))
    for x in range(-100, 100):
        f = ((x not in a) or (x in p)) or (x in q)
        if not f:
            return False
    return True


for a in range(1, 100):
    if func([a]):
        print(a)
def func(a):
    p = list(range(10, 40+1))
    q = list(range(5, 15+1))
    r = list(range(35, 50 + 1))
    for x in range(-100, 100):
        f = ((x not in p) or (x in q)) or ((x not in a) or (x in r))
        if not f:
            return False
    return True


for a in range(1, 100):
    if func([a]):
        print(a)
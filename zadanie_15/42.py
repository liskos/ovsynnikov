def func(a):
    p = list(range(10, 26))
    q = list(range(0, 13))
    for x in range(-100, 100):
        f = (x in a) or (x not in p) or (x in q)
        if not f:
            return False
    return True


print(func(list(range(10, 16))))
print(func(list(range(20, 36))))
print(func(list(range(5, 21))))
print(func(list(range(12, 41))))
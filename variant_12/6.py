def func(d):
    n = 8
    s = 6
    while s <= 1800:
        s = s + d
        n = n + 7
    return n


for i in range(1, 10000):
    if func(i) == 246:
        print(i)
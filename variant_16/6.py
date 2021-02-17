def f(d):
    n = 20
    s = 40
    while s + n < d:
        s = s - 10
        n = n - 20
    return n


for i in range(10000, 1, -1):
    if f(i) > 0:
        print(i)
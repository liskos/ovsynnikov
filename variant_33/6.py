def f(n):
    s = 155
    while s - n > 0:
        s = s - 5
        b = n + 10
    return s


for i in range(1, 10000):
    if f(i) == 145:
        print(i)
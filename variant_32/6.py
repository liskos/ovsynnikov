def f(s):
    n = 1
    while s < 47:
        s = s + 4
        n = n * 2
    return n


for i in range(1, 1000):
    if f(i) == 64:
        print(i)



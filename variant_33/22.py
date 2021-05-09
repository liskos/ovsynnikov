def f(x):
    l = 1
    m = 0
    while x > 0:
        m = m + 1
        if x % 2 == 0:
            l = l * (x % 8)
        x = x // 8
    return l, m


for i in range(1, 10000):
    l, m = f(i)
    if l == 12 and m == 3:
        print(i)
def f(x):
    l = x - 16
    m = x + 16
    while l != m:
        if l > m:
            l = l - m
        else:
            m = m - l
    return m


for i in range(100,10000):
    if f(i) == 16:
        print(i)
        break
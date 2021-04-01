def f(x):
    l = x - 18
    m = x + 36
    while l != m:
        if l > m:
            l = l - m
        else:
            m = m - l
    return m


for i in range(100, 1000):
    if  f(i) == 9:
        print(i)
        break

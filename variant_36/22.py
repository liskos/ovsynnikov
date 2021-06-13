def f(x):
    L = x
    M = 55
    if L % 2 == 0:
        M = 44
    while L != M:
        if L > M:
            L = L - M
        else:
            M = M - L
    return M


for i in range(80, 10000):
    if f(i) == 22:
        print(i)
        break

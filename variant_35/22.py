def f(x):
    L = x - 12
    M = x + 12
    while L != M:
        if L > M:
            L = L - M
        else:
            M = M - L
    return M

for i in range(100, 1000):
    M = f(i)
    if M == 2:
        print(i)
        break
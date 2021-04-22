def f(x):
    Q = 9
    L = 0
    if x < Q:
        t = x
        x = Q
        Q = t
    while x >= Q:
        L = L + 1
        x = x - Q
    M = x
    return L, M


for i in range(1, 1000):
    L, M = f(i)
    if L == 4 and M == 1:
        print(i)
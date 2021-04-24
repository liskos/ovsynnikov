def f(S):
    N = 2
    while S <= 234:
        S = S + N
        N = N + 3
    return N

for i in range(1, 10000):
    if f(i) == 32:
        print(i)

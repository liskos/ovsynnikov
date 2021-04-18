def f(d):
    S = 5
    N = 7
    while S <= 3011:
        S = S + d
        N = N + 124
    return N


k = 0
for i in range(1,10000):
    if f(i) == 1247 and i % 10 == 8:
        k +=1
print(k)


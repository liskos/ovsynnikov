def f(x):
    L = 0
    M = 0
    while x > 0:
        M = M + 1
        if x % 2 != 0:
            L = L + 1
            x = x // 2
    return L, M

k = 0
for i in range(100, 1000):
    L,M = f(i)
    if a == 5 and b == 8:
        k += 1
print(k)
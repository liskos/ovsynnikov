def f(x):
    x = int(input())
    L, M, R = 0, 0, 0
    while x > 0:
        R = R * 10 + x % 10
        x = x // 10
        if x <= R:
            M = M + 1
        else:
            L = L + x % 10
    return L, M


for i in range(1, 10000):
    if f(i)== 14 and f(i)==3:
        print(i)
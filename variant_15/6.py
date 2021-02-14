def f(d):
    n = 50
    s = 101
    while n + d < s:
        s = s + 50
        n = n - 10
    return n


for i in range(1, 10000):
    if f(i) == 50:
        print(i)
        break
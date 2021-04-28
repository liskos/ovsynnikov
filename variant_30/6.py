def f(d):
    n = 7
    s = 35
    while s <= 2570:
        s = s + d
        n = n + 9
    return n


k = 0
for i in range(-100, 10000):
    if f(i) == 196:
        k +=1
print(k)
def f(d):
    s = 15
    n = 10
    while s <= 2400:
        s = s + d
        n = n + 5
    return n


k = 0
for i in range(1, 1000):
    if f(i) == 50 and f(i) % 10 == 0:
        k +=1
print(k)

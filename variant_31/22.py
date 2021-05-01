def f(x):
    a = 0
    b = 1
    while x > 0:
        if x % 2 > 0:
            a = a + x % 11
        else:
            b = b * (x % 11)
        x = x // 11
    return a, b


k = 0
for i in range(100, 1000):
    a,b = f(i)
    if a == 5 and b == 12:
        k += 1
print(k)


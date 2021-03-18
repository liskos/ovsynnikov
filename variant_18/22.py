def f(x):
    a = 0
    b = 0
    while x > 0:
        if x % 2 == 1:
            a = a + 1
        else:
            b = b + 1
        x = x // 10
    return a, b


for i in range(100, 1000000000):
    a, b = f(i)
    if a == 1 and b == 4:
        print(i)

def f(x):
    a = 0
    b = 0
    while x > 0:
        a += 1
        b += x % 8
        x = x // 8
    return a, b



for i in range(100, 39, -1):
    a, b = f(i)
    if a == 3 and b == 24:
        print(i)
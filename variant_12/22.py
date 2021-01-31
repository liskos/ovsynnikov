def func(x):
    a = 0
    b = 1
    while x > 0:
        if x % 2 > 0:
            a += 1
    else:
        b += x % 5
    x = x // 5
    return a, b



for i in range(1, 10000):
    a, b = func(i)
    if a == 2 and b == 12:
        print(i)
        break
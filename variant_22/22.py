def f(x):
    a = 0
    b = 0
    while x > 0:
        a += 1
        b += x % 10
        x = x // 10
    return a, b


for i in range(1, 100000):
    a, b = f(i)
    if a == 2 and b == 9:
        print(i)
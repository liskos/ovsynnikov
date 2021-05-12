def f(x):
    a = 1
    b = 10
    while x > 0:
        c = x % 10
        a = a * c
        if c < b:
            b = c
        x = x // 10
    return a,b


for i in range(1, 1000):
    a,b = f(i)
    if a == 45 and b == 5:
        print(i)
        break
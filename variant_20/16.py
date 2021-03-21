def f(n):
    if n > 30:
        return n * n + 5 * n + 4
    elif n <= 30:
        return f(n+1) + 3 * f(n+4)
    elif n <= 30:
        return 2 * f(n + 2) + f(n + 5)


count = 0
for i in range(1, 1001):
    x = f(i)
    s = 0
    while x > 0:
        s += x % 10
        x = x // 10
    if s == 27:
        count += 1
        m = count
print(count)




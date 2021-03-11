def f(n):
    if n <= 18:
        return n + 3
    elif n % 3 == 0:
        return (n // 3) + f(n//3) + n - 12
    else:
        return f(n-1) + n*n + 5


r = 0
for i in range(1, 1001):
    x = f(i)
    ch = True
    while x > 0:
        ch = ch and (x % 2 == 0)
        x = x // 10
    if ch:
        r += 1
print(r)
def f(n):
    if n <= 15:
        return n * n + 11
    if n > 15 and n % 2 == 0:
        return f(n//2) + n * n * n - 5 * n
    if n > 15 and n % 2 == 1:
        return f(n - 1) + 2 * n + 3


k = 0
for i in range(1, 1001):
    c6 = 0
    x = f(i)
    while x > 0:
        if x % 10 == 6:
            c6 += 1
        x = x // 10
    if c6 >= 3:
        k +=1
print(k)

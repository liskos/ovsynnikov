def f(n):
    if n > 30:
        return n * n + 5 * n + 4
    elif n % 2 == 0 and n <= 30:
        return f(n+1) + 3 * f(n+4)
    elif n % 2 != 0 and n <= 30:
        return 2 * f(n + 2) + f(n + 5)


count = 0
for i in range(1, 1001):
    a = map(int, str(f(i)))
    if sum(a) == 27:
        count += 1
print(count)




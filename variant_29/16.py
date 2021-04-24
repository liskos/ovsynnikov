def f(n):
    if n < 3:
        return n + 1
    if n >= 3 and n % 2 == 0 :
        return n + 2 * f(n + 2)
    if n >=3 and n % 2 != 0:
        return f(n-2) + n - 2

print(f(100))
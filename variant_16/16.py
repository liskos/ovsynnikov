def f(n):
    if n < -98:
        return 1
    elif n > 10:
        return f(n-1) + 3*f(n - 3) + 2
    else:
        return -f(n - 1)


print(f(20))


def f(n):
    if n < 50:
        return n
    else:
        return 2 * g(50 - n//2)
def g(n):
    if n > 40:
        return 10
    else:
        return 30 + f(n + 600 // n)



print(f(80))
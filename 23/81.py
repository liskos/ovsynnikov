def f(a,b):
    if a == b:
        return 1
    if a > b or a == 21:
        return 0
    return f(a +1, b) + f(2 * a +1, b)

print(f(1, 25))
def f(a,b):
    if a == b:
        return 1
    if a > b or a == 10:
        return 0
    return f(a +1, b) + f(a + 3, b)

print(f(3, 15) * f(15, 20))
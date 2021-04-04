def f(x):
    return abs(x-4)+abs(x+6)-3


def func(d):
    a = -20
    b = 20
    c = 1
    for t in range(a, b+1):
        if f(t) < d:
            c = c +1
    return c


k = 0
for d in range(1, 100000):
    if func(d) < 15:
        k += 1
print(k)
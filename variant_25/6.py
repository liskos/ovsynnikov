def f(s):
    for k in range(4, 8):
        s *= k
    return s


for i in range(1, 10000):
    if f(i) > 18500:
        print(i)
        break
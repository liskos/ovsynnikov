def f(s):
    n = 200
    while s // n >= 2:
        s = s + 5
    n = n + 5
    return


for i in range(1, 100000):
    if f(i) in range(100, 1000):
        print(i)
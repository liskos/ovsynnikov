def f(x):
    s = 0
    while x > 0:
        if x % 2 > 0:
            s = s + (x % 7)
        else:
            s = s - (x % 7)
        x = x // 7
    return s



k = 0
for i in range( 51, 1000):
    if f(i) == 1:
        print(i)
        break
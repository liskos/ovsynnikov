def f(x):
    p = 90
    s = 6 * (x - x % 22)
    k = 0
    while p < 181:
        k = k + 1
        p = p + k
        s = s - 2 * k
    return s



for i in range( 51, 1000):
    if f(i) == 82:
        print(i)




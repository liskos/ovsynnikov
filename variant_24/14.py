def f(x,y):
    z = 2*7**x + 3 * 7**(x+1) + 4* 7**(x+2) + 5*7**y + 6*7**(2*y)
    s = 0
    while z > 0:
        s += z % 7
        z = z // 7
    return s

def min_f():
    minf = 99999999
    for x in range(1, 100):
        for  y in range(1, 100):
            r = f(x,y)
            if r < minf:
                minf = r
    return minf

def kol_f(n):
    k = 0
    for x in range(1, 100):
        for  y in range(1, 100):
            if f(x, y) == n:
                k += 1
    return k

print(kol_f(min_f()))
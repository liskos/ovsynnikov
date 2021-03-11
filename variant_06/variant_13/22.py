def f(x):
    s = 1
    a = 11
    while x // 7 > 0:
        if x % 7 < 4:
            s = s + a
        else:
            s = s + (x % 7)
        x = x // 7
    return  s

minn = 2000000
ind = 0
for i in range(26, 10000):
    if f(i) > 25 and f(i)< minn:
        minn = f(i)
        ind = i
print(ind)

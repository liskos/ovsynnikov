def f(x):
    s= 0
    while x > 0:
        if x % 5 > 0:
            s = s + (x % 5)
        else:
            s = s * (x % 5)
        x = x // 5
    return s

k = 0
for i in range(1, 501):
    if f(i) == 13:
        k +=1
print(k)
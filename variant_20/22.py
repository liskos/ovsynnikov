def f(x):
    l = 0
    m = 1
    while x > 0:
        l = x % 10 * m + l
    x = x // 10
    m = m * 10
    return l


count = 0
for i in range(1, 1000000):

    if f(i) == 15:
        count += 1
print(count)


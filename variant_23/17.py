k = 0
m = 0
for i in range(9999, 99999 + 1):
    x = i
    s = 0
    while x > 0:
        s += x % 10
        x = x // 10
    if i % s == 0:
        k +=1
        m = i

print(k, m)

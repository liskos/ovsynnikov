def f(d):
    n = 0
    s = 24
    while s <= 1318:
        s = s + d
        n = n + 15
    return n

mass = []
for i in range(1, 1000):
    if f(i) == 195:
        mass.append(i)
print(min(mass), max(mass))
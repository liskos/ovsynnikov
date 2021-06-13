def f(d):
    n = 33
    s = 4
    while s <= 1725:
        s = s + d
        n = n + 8
    return n


mass = []
for i in range(1, 1000):
    if f(i) == 153:
        mass.append(i)
print(max(mass), min(mass))
def func(x, prost):
    a = []
    for i in prost:
        if x % i == 0:
            a.append(i)
    return a


def delit(x):
    a = []
    for i in range(2, x):
        for j in a:
            if i % j == 0:
                break
        else:
            a.append(i)
    return a


a = 25317
b = 51237
prost = delit(b+1)
print(prost)
for i in range(a, b+1):
    mass = func(i, prost)
    if len(mass)>=6:
        print(i, max(mass))
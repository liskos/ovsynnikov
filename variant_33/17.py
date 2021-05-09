k = 0
mass = []
for i in range(800, 5901):
    if i % 19== 0 and i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
        k+=1
        mass.append(i)
print(k, max(mass))
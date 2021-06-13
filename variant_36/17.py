k = 0
mass = []
for i in range(1016, 7938):
    if i % 3 == 0:
        if i % 7 != 0 and i % 17 != 0 and i % 19 != 0 and i % 27 != 0:
            k +=1
            mass.append(i)
print(k, max(mass))
k = 0
m = []
for i in range(16015, 48989 +1):
    if i % 7 == 0 and i % 11 == 0:
        if i % 9 != 0 and i % 12 != 0 and i % 13 != 0:
            k +=1
            m.append(i)
print(k, min(m))
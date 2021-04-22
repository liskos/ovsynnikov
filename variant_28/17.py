c, m = 0, 0


for i in range(3089, 9716):
    if i %2 ==0:
        if (i % 7) * (i % 8) * (i % 9) * (i % 13) != 0:
            c += 1
            m = i

print(c, m)
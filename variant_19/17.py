minn = []
k = 0
for i in range(1200, 11201):
    if i % 5 == 0 and i % 7 != 0 and i % 13 != 0 and i % 17 != 0 and i % 19 != 0:
        k += 1
        minn.append(i)
print(k, min(minn))

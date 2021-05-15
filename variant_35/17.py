k = 0
for i in range(1170, 8368):
    if i % 3 == 0 and i % 7 == 0:
        if i % 11 != 0 and i % 13 != 0 and i % 19 != 0 and i % 17 != 0:
            k +=1
    print(k, i)
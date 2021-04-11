k = 0
for i in range(2476,  7858):
    if i % 2 == 0 and i % 8 == 0:
        if (i // 100 % 10) <= 7:
            k +=1
print(k)

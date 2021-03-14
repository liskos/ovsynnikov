a = []
for i in range(2476,  7858):
    if i % 2 == 0 and i % 8 != 0 and (i // 100)%10 <= 7:
        a.append(i)
print(len(a), (a[0]+a[-1])/2)
a = []
for i in range(1234567, 7654321+1):
    s = str(i)
    razn = abs(int(s[:2]) - int(s[-2:]))
    if razn != 0 and i % razn == 0 :
        a.append(i)
print(len(a), max(a))
a = []
for i in range(1005, 147870+1):
    x = max(map(int, str(i))) - min(map(int, str(i)))
    if "1" not in str(i) and x < 4:
        a.append(i)
print(len(a), a[-25])
a = []
for i in range(333666, 666999 +1):
    if i % 17 == 0 and str(i).count("7") >= 2:
        a.append(i)
print(max(a))
print(len(a))
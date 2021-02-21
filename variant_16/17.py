a = []
for i in range(12345, 54321+1):
    if i % 13 == 0 and i % 7 != 0 and i % 9 != 0 and i % 11 != 0:
        a.append(i)
print(min(a)*256*256, len(a))
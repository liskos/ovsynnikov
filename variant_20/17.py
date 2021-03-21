k = 0
m = 0
for i in range(1000, 70001):
    if 8**5 > i >= 8**4 and 5**6 > i >= 5**5 and (i %(16**2)) == 15* 16 + 10:
        k +=1
        m = i

print(k, m)
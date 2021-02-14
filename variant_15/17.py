a = []
for i in range(1032, 8416):
     a1 = i % 100
     a2 = i // 100
     razn = max(a1, a2) - min(a1, a2)
     if a1 >= 10 and a2 >= 10 and razn > 70:
          a.append(i)
print(max(a), len(a))
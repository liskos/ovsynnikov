k = 0
summ = []
for i in range(3672, 9118):
    if i % 3 == 2 and i % 5 == 4:
        k +=1
        summ.append(i)
print(k, sum(summ))

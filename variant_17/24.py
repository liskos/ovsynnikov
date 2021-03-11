file = open(file="Задание 24/24.txt")

k = 0
for s in file:
    n = 0
    for z in "QWERTYUIOPASDFGHJKLZXCVBNM":
        b = "Z"+z + "RO"
        if b in s:
            n += 1
            break
    if n > 0:
        k += 1
print(k)
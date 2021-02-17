x = 4 * 7**103 - 21 * 7**57 + 98
s = ""
summ = 0
while x > 0:
    s = str(x % 7) + s
    x //= 7
    summ += x

print(summ)
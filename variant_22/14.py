x = 7**28 + 49**24 - 7**2
s = ""
while x > 0:
    s = str(x % 7) + s
    x //= 7
print(s.count("6"))
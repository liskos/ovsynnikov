x = (24400 - 1) * (42200+2)
s = ""
while x > 0:
    s = str(x % 2) + s
    x //= 2
print(s.count("1"))
x = 5**94 + 25**49 - 130
s = ""
while x > 0:
    s = str(x % 5) + s
    x //= 5
print(s.count("4"))
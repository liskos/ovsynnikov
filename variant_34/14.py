x = 25**5 + 5**15 - 25
s = ''
while x > 0:
    s = str(x%5)+s
    x = x // 5
print(s.count("4"))
x = 7**103 + 49**98 - 7**120 - 7**33
s = ''
m = []
while x > 0:
    s = str(x%7)+s
    x = x // 7
    m.append(s)
print(s)
x = 81**2017 + 9**5223 - 81
s = ''
while x > 0:
    s = str(x%9)+s
    x = x // 9
print(s.count("8"))
x = 16**8 * 4**20 - 4**10 - 4
s = ''
while x > 0:
    s = str(x%4)+s
    x = x // 4
print(s.count("3"))
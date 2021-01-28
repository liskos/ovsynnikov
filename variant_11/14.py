def devyt(x):
    s = ""
    while x > 0:
        s = str(x % 9) + s
        x = x // 9
    return s

for i in range(1, 10000):
    s = devyt(i)
    s2 = devyt(i*3)
    if len(s)==3 and s.count("3")>0 and len(s2) == 3:
        print(i)

print(devyt(237+84))
file = open(file="Задание 24/24.txt", mode="r")

a = []
for s in file:
    m = s[0]
    for i in range(1, len(s)):
        if int(s[i-1])+int(s[i])>=10:
            m += s[i]
        else:
            a.append(m)
            m = s[i]
a.append(m)
b = []
for i in a:
    b.append(len(i))
print(max(b))
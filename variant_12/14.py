x = 3627 + 618 - 19
s = ""
while x > 0:
    s = str(x % 6) + s
    x //= 6
print(s.count("0"))7
s = "1" * 106
while "333" in s or "111" in s:
    s = s.replace("333", "11", 1)
    s = s.replace("111", "3", 1)

print(s)
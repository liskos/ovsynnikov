s = "1" * 100
while "111" in s:
    s = s.replace("111", "2", 1)
    s = s.replace("2222", "333", 1)
    s = s.replace("33", "1", 1)
print(s)
s = "8" * 84
while "777" in s or "888" in s:
    if "777" in s:
        s = s.replace("777", "8", 1)
    else:
        s = s.replace("888", "7", 1)
print(s)
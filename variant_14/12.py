s = "1" * 20 + "0" * 20 + "<"
while "0<" in s or "1<" in s:
    if "11<" in s or "10<" in s:
        if "11<" in s:
            s = s.replace("11<", "<3", 1)
        else:
            s = s.replace("10<", "<2", 1)
    else:
        if "00<" in s:
            s = s.replace("00<", "<0", 1)
        if "01<" in s:
            s = s.replace("01<", "<1", 1)
print(s)
print(3+3+3+3+3+3+3+3+3+3)
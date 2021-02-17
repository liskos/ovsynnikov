s = ">" + "432" * 100 + "<"
while ">4" in s or ">3" in s or ">2" in s or "4<" in s or "3<" in s or "2<" in s:
    if ">4" in s or ">3" in s:
        s = s.replace(">4", "2>3", 1)
        s = s.replace(">3", "1>2", 1)
    else:
        if "4<" in s or "3<" in s:
            s = s.replace("4<", "3<2", 1)
            s = s.replace("3<", "2<1", 1)
        else:
            s = s.replace(">2", "0>", 1)
            s = s.replace("2<", "<0", 1)
print(s)
print(s.count("2"))
print(s.count("1"))
print(100 * 2 + 200)
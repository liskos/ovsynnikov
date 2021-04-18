s = ">" + "1" * 20 + "2" * 15 + "3" * 40 + "<"
while "><" in s:
    s = s.replace(">1", "3>", 1)
    s = s.replace(">2", "2>", 1)
    s = s.replace(">3", "1>", 1)
    s = s.replace("3<", "<1", 1)
    s = s.replace("2<", "<3", 1)
    s = s.replace("1<", "<2", 1)
print(s)
print(  (s.count("2")* 2) + (s.count("3")*3))
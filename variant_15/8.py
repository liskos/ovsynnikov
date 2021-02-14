k = 1
for s1 in "АВДПР":
    for s2 in "АВДПР":
        for s3 in "АВДПР":
            for s4 in "АВДПР":
                s = s1 + s2 + s3 + s4
                print(k, s)
                k += 1
                if ("А" not in s) and len(set(list(s)))==4:
                    print("+")
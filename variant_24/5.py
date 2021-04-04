def alg(x):
    x = bin(x)[2:]
    if x.count("1") > x.count("0"):
        x += "0"
    else:
        x += "1"
    n = len(x)
    if n % 2 == 0:
        r = x[:n//2-1] + x[n//2+1:]
    else:
        r = x[:n//2-1] + x[n//2+2:]
    return int(r,2)


for i in range(15, 1000):
    if alg(i) == 55:
        print(i)
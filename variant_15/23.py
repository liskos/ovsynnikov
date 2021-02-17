def f(a, b):
    if b < a:
        return  0
    if b == a:
        return 1
    if str(b)[-1] == "1" and len(str(b))> 1:
        return f(a, b -2) + f(a, b -3) + f(a, b //10)
    else:
        return f(a, b -2) + f(a, b -3)

print(f(3,12)*f(12,25))
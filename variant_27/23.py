def f(a,b):
    if a== b:
        return 1
    if a > b:
        return 0
    if a % 2 ==0:
        c = a + 1
    else:
        c = a + 2
    return f(a+1,b)+f(a*2,b)+f(a+c,b)


print(f(3, 25)*f(25,75))
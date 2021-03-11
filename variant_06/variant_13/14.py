def f(x):
    return 3 * 7 **(x+1) + 13 * 7 ** (x+2) + 31*7**(3*x) + 1 * 7 **(2*x)


def sem(x):
    s = 0
    while x >0:
        s += x % 7
        x = x // 7
    return s


for x in range(0, 100):
    if sem(f(x)) == 18:
        print(x)
        break
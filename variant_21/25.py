def pr(i):
    for j in range(2, i):
        if i % j == 0:
            return False
    return True


k = 0
for i in range(6638225, 6638322+1):
    if pr(i):
        k += 1
        print(k, i)

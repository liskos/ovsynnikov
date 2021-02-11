m = 0
c = 0
for i in range(246815, 875622):
    if (i // 100) % 100 < 50:
        if(i%1000) % 5 == (i//1000)% 5:
            c += 1
            m = i
print(c, m)
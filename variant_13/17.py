k = 0
for i in range(12345, 54322):
    if i % 3 == 2 or i % 5 == 6 and i % 9 == 8 and i % 10 != i // 10000:
        print(i)
        k += 1
print("k =", k)
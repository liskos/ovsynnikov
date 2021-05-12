n = 0
str='ЕЖЗИ'
for s1 in str:
  for s2 in str:
    for s3 in str:
      for s4 in str:
          if  (s1 + s2 + s3 + s4).count("Е") == 1 or (s1 + s2 + s3 + s4).count("И") == 1:
              n +=1
print(n)
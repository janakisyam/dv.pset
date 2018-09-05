n = 2000000
primenumber = []
sum = 0
for i in range (0,n):
  if i > 1:
    for j in range(2,i):
      if (i%j==0):
        break
    else:
      primenumber.append(i)
print(primenumber)
for i in range (len(primenumber)):
    sum = sum + primenumber[i]
print(sum)

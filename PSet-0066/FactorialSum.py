n = 100
fact = 1
for n in range (100,1,-1):
    fact = fact * n
sum = 0
n = str(fact)
for i in range(0,len(n)):
    sum = sum + int(n[i])
print(sum)


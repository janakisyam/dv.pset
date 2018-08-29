n = []
s = 0
for i in range (0,100):
    if (i%5==0) or (i%3==0):
        n.append(i)
print(n)

for j in range(len(n)):
    s = s + n[j]
print(s)

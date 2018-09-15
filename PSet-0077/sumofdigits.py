x= int(input("Enter number: "))
n = str(x)
sum = 0
for i in range(len(n)):
    sum = sum + int(n[i])
print(sum)

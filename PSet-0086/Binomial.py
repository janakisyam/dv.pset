a = ["x"]
b = ["y"]
start = [1]
k=0
pow = int(input("Enter power: "))
print("(x + y)^" +str(pow))
for i in range(pow):
    #print("\n")
    binomial = []
    binomial.append(1)
    for i in range(0,len(start)-1):
        binomial.append(start[i]+start[i+1])
    binomial.append(1)
    start = binomial
for j in range(pow,-1,-1):
    print(start[j],end=" * ")
    print(*a,end="^")
    print(j,end=" * ")
    print(*b,end="^")
    print(k,end=" + ")
    print(end=" ")
    k+=1
 #prints the row of coefficients

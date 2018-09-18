#findSumOfDigits(x)
def findSumOfDigits(x,y):
    n = str(x)
    n1 = str(y)
    sumx = 0
    sumy = 0
    for i in range(len(n)):
        sumx = sumx + int(n[i])
    for j in range(len(n1)):
        sumy = sumy + int(n1[j])
    if (sumx == sumy):
        print(1)
    else:
        print(0)

x = int(input("Enter number: "))
y = int (input("Enter number:"))
findSumOfDigits(x,y)

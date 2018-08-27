#bubblesort
list = [1,5,3,6,7,8,2,10,4,9]
print(list)
n = len(list)
for i in range (n):
    for j in range (n-i-1):
        if (list[j] > list[j+1]):
            swap = list[j]
            list[j] = list[j+1]
            list[j+1] = swap
        i+=1
print("Sorted list is: " +str(list) )

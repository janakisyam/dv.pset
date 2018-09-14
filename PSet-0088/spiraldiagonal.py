# each of the spiral elements is added by even numbers
# the number of elements goes till 200 becuase 1 is repeated
sum = 0
list = []
n = 2
num = 1
for i in range(0,500): #the total number of rings
    for j in range(0,4): # to find each ring of 4 digits
        num = num + n
        list.append(num)
    n+=2 #adding with even numbers
for j in range(len(list)):
    sum = sum + list[j] #adding elements
print(sum+1) #adding the middle 1

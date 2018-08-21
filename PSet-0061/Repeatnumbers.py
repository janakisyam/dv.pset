list=[]
list1=[]
for x in range (10):
    a=int(input())
    list.insert(x,a)
    x = x + 1
for i in range (10):
    for j in range (i):
        if (list[i]==list[j]):
            j+=1
            list1.append(list[i])
print(list1)

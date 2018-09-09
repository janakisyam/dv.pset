list = []
for i in range (5):
    x = int(input("Enter numbers: "))
    list.append(x)
flag = 0
flag1 =0
'''for j in range (0,len(list)-1):
    for k in range(j+1,len(list)):
        #flag = 1 doesnt work as it is true if first digit satisfies
        if list[j] > list[k]:
            flag = 1
            break
        if list[j] < list[k]:
            flag = 2
            break
'''
for j in range (0,len(list)-1):
    for k in range(j+1,len(list)):
        if list[j] > list[k]:
            flag+=1
            break
        if list[j] < list[k]:
            flag1+=1
            break
    '''else:
        flag= 0
        break
    k+=1'''
if (flag == 4):
    print("Descending Order")
elif flag1 == 4:
    print("Ascending Order")
else:
    print("None")

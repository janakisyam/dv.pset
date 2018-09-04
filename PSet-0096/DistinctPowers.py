#final=[]
list = []
count = 1
#flag = True
for a in range (2,101):
	for b in range(2,101):
		list.append(a**b)
for i in range(0,len(list)): #values of the list
	for j in range(i+1,len(list)): #values incrimented by one
		if list[i] == list[j]:#check if same with all list elements
			list[i]=0 #if same, equate to 0
for i in range(len(list)-1):
	if list[i] != 0: # if different count the distinct
		count+=1
print("The distinct powers are: ")
print(count)

'''for a**b in list:
	if a**b not in final:
		final.append(a**b)'''

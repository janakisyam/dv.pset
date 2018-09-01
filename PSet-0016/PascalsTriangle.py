#pascal=[]
start = [1]
#s = ' '
rows = int(input("Number of rows: "))
space = 2*rows-2
for i in range(rows):
	for j in range(0,space):
		print(" ",end='')
		#print("working")
	space-=1
	print(*start)
	print("\n")
	pascal = []
	pascal.append(1)
	for i in range(len(start)-1):
		pascal.append(start[i] + start[i+1])
		#break
	pascal.append(1)
	start = pascal
#print(start)

#old code
'''#pascal = []
start = [1]
rows = int(input("Number of rows: "))
#space = 2*rows-2#total number of spaces
for i in range(0,rows-1):
	for j in range(0,i+1): #print pascals triangle
		print(*start,end=" ")
		print(end='\n')
		pascal = []
		pascal.append(1)#adds always one at beginning
		for i in range(len(start)+1):
			pascal.append(start[i-1] + start[i]) #adding the adjacent digits to each other
			#break
		pascal.append(1) # adds one always at the end
		#start = pascal
		start=pascal'''

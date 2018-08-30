#pascal = []
start = [1]
rows = int(input("Number of rows: "))
for i in range(rows):
	print(start)
	pascal = []
	pascal.append(1)
	
	for i in range(len(start)-1):
		pascal.append(start[i] + start[i+1])
		#break
	pascal.append(1)
	start = pascal
#print(start)


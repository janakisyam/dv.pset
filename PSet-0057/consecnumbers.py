'''n = int(input("Number of Rows: "))
num = 1
for i in range(n):
	for j in range(n):'''

i=0;
num = 1
rows=int(input("Number of rows: "))
for i in range(0,rows):
  for j in range (0,i):
    print(num,end=' ')
    num+=1
  print(' ')
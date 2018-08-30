n = 1000
for a in range(1,n+1):
	for b in range(1,a+1):
		sidesum=a+b
		c = 1000 - sidesum
		if(a*a + b*b == c*c):
			print(a,b,c)
			product = a*b*c
			print(product)

import random
print("Five random numbers are: ")
num1 = random.randint(0,1000)
for i in range(0,5):
	num2 = random.randint(0,1000)
	if (num2 != num1):
		print(num2)
	i+=1

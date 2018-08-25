import random
m = input("Enter a range, and I will pick a random number from it:  ")
r = random.randint(0,int(m))
x = True
count = 0
while True:
    guess = int(input("Guess the number I picked: "))
    if (guess > r):
        print("High")
        x = False
        count+=1
        continue
    elif (guess < r):
        print("Low")
        x = False
        count+=1
        continue
    elif (guess == r):
        print("Correct")
        x = True
        count+=1
        break

print("Number of times taken to  guess the right answer: " +str(count))

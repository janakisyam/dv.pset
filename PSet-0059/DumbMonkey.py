ladder = int(input("Enter number of Steps: "))
if ladder > 3:
    if (ladder % 2 == 0):
        print("NO")
    else:
        print("YES")
elif ladder <=3:
    print("NO")

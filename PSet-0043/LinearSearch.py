list=[4,2,7,5,1,9]

search = int(input("Number to search for: "))

flag = False
position = 0
for i in range (len(list)):
    if search == list[i]:
        flag = True
        print("The number is at position: " +str(position))
        break
    position = position + 1
if not flag:
    print("Number is not in list.")

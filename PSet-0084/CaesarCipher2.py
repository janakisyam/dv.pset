ROT0 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#ROT0 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
rot = []
space = ' '
rotation_number = int(input("Enter rotation number: "))
for i in range(rotation_number,len(ROT0)):
    rot.append(ROT0[i])
    i+=1
for i in range(0,rotation_number):
    rot.append(ROT0[i])
    i+=1
print(rot)
message = input("Enter message to decrypt: ")
start = 0
decrypt = []
for i in range (0,len(message)):
    for j in range (0,len(rot)):
        if message[i]==rot[j]:
            #rn = ROT0[j]-rotation_number
            decrypt.append(ROT0[j])
            break
        else:
            j+=1
    if message[i] == ' ':
        decrypt.append(space)

print(*decrypt)
print("\n")

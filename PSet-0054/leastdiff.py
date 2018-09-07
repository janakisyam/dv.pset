import math
print("Enter: ")
s = []
diff = 100
for x in range(10):
    num = input()
    s.append(num)
for i in range(0,len(s)):
    for j in range(i+1,len(s)):
        '''if(s[i]>s[j]):
            diff.append(int(s[i])-int(s[j]))
        elif(s[i]<=s[j]):
            diff.append(int(s[j])-int(s[i]))'''
        if abs(int(s[i]) - int(s[j])) < diff:
            diff = abs(int(s[i])-int(s[j]))
            print("The least difference is:" +diff)

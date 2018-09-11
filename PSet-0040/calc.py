def ADD(x,y):
    sum = x + y
    print(sum)
    return sum
def SUB(x,y):
    if (x > y):
        diff = x - y
    else:
        diff = y - x
    print(diff)
    return diff
def MULT(x,y):
    mult = x*y
    print(mult)
    return mult
def DIV(x,y):
    div = x/y
    print(div)
    return div
print("What would you like to do? ")
print("1. ADD")
print("2. SUBRTACT")
print("3. MULTIPLICATION")
print("4. DIVIDE")
x = int(input("Enter one number: "))
y = int(input("Enter one number: "))
choice = int(input("Enter operation: "))
if (choice == 1):
    ADD(x,y)
elif (choice == 2):
    SUB(x,y)
elif (choice == 3):
    MULT(x,y)
elif (choice == 4):
    DIV(x,y)

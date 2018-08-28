num1 = int(input("Input numerator of fraction 1: "))
den1 = int(input("Input denominator of fraction 1: "))
num2 = int(input("Input numerator of fraction 2: "))
den2 = int(input("Input denominator of fraction 2: "))

if (den1 == den2):
    den = den1
    num = num1 + num2
    print("The sum is:")
    print(num)
    print("--")
    print(den)
else:
    den = den1 * den2
    num = num1 + num2
    print("The sum is:")
    print(num)
    print("--")
    print(den)

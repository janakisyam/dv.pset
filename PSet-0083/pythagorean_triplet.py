print("Condition a<b<c")
a = input("Input first side: ")
b = input("Input second side: ")
c = input("Input third side: ")

sum_of_sides= int(a) * int(a) + int(b) * int(b)

square_of_hypotnuse = int(c) * int(c)

if(sum_of_sides == square_of_hypotnuse):
  print("True. It forms a pythagorean triplet.")
else:
  print("False. It does not form a pythagorean triplet.")

print("Multiplication table maker")

num = eval(input("Enter a number -->: "))

for i in range (1, 11):
  mul = num * i
  print(num, "x", i, "=", mul)
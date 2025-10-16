#using f and {}
#string formatting

#fname = 'Bry'
#mname = 'Zuniga'
#lname = 'Echevarria'

#print(f"My name is {fname} {mname} {lname} ")

oddSum = 0

for i in range(1,11):
  num = eval(input("Input a number :" ))

  if num % 2 == 1:
    oddSum += num
    
print(f"The sum of odd number is {oddSum}")
#Write a program that asks the user to enter 10 numbers, and then prints the sum of those numbers.

num = 0 
for i in range (1, 11, 1):
    number = eval(input ('please enter a number:'))
    num += number
print ('the sum of the number is :', num)
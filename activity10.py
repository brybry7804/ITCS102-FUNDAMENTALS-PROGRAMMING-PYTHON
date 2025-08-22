name = input("Input your name ---> ")
isStudent = input("Are you a student (Yes / No) --> ")
fare = eval(input("bayad --> "))

if isStudent == "yes" :
        discount = fare * .2
        print("Hi", name, " student discount  is ", discount)
else:
        print("Sorry ", name," you are not eligible for student discount")
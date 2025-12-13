name  = input("Name: ")

print(f"hi {name}, welcome to my file compiler")


while True:
    print("----------------------------------------------------------")
    print("\t\t\tSelect a program \n----------------------------------------------------------")
    print("A - Activity 1\nB - Activity 2\nC - Activity 3\nD - Activity 4\nE - Exit")

    ask = input("\n\tWhich program would you like to run: ").lower()

    if ask == "a":
        activity1()
        continue
    elif ask == "b":
        activity2()
        continue
    elif ask == "c":
        activity3()
        continue
    elif ask == "d":
        activity4()
    elif ask == "e":
        print("thank you for visiting! ")
        break
    else:
        print("try again")
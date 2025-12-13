import random,time

print("let's start the game :D")
time.sleep(1)
r = input("you ready? :) --> ")

random_number = random.randint(1, 100)
tries = 0
con = True

while True:
    num = int(eval(input("Input your number - - - > ")))

    con += 1 

    if num == random_number: 
        print("you're correct!")
        print(f"hahahah it only took {con} tries")
        break
    else:
        print("that's wrong!")
        print("try again...")
        continue
temp = eval(input("Enter Temperature: "))
if temp >= 1 and temp <= 20:
        print("The temperature outside is cold ")

elif temp >= 21 and temp <= 30:
        print("The temperature outside is lukewarm ")

elif temp >= 31 and temp <= 40:
        print("The temperature outside is warm ")

elif temp >= 41 and temp <= 50:
        print("The temperature outside is hot ")

elif temp >= 51 and temp <= 60:
        print("The temperature outside is boiling hot ")

else:   print("The temperature is Invalid ")

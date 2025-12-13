s = True

empty_dictionary = { }

def shortcut_po():
    for w,m in empty_dictionary.items():
        print(f"word -- {w}, meaning -- {m}")


while s == True:
    shortcut = input("Enter the shortcut letter: ")
    word = input("What's the meaning? : ")

    empty_dictionary[shortcut] = word

    tanong = input("Would you like to continue?   (YES/NO): ")

    if tanong ==  'yes'.lower():
        print("wait lang")
        continue
    elif tanong == 'no'.lower():
        print("gegege")
        shortcut_po()
        break
    else:
        print("error yan beh")

        
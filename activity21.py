while True:
    music = input("Do you want to continue listening to the playlist? (yes/no) --> ").lower()

    if music == 'yes':
        print("Playing the next song..\n")
        continue
    elif music == 'no':
        print("I'm stopping the music now..\n")
        break
    else:
        print("Huh? Please answer the question properly\n")
        continue
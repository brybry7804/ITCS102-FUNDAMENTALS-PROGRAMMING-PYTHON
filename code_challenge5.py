name = input("Enter your name: ")
print("Welcome to the Manga Reader Recommender", name, "!!!")
print("\n!AVAILABLE GENRES!\n'action - romance - horror'")

genre_choice = input("Please input genre type: ")

if genre_choice.lower() == "action":
    print("You have selected Action")
    time = input("What year (2000s, 2010s): ")

    if time == "2000s":
        short_medium_long = input("How long should the manga be? (short, medium, long): ")

        if short_medium_long.lower() == "short":
            print("Recommendation: 'Tokyo Ghoul'")
        else:
            if short_medium_long.lower() == "medium":
                print("Recommendation: 'Uzumaki'")
            else:
                if short_medium_long.lower() == "long":
                    print("Recommendation: 'Naruto'")

    else:
        if time == "2010s":
            short_medium_long = input("How long should the manga be? (short, medium, long): ")

            if short_medium_long.lower() == "short":
                print("Recommendation: 'Darling in the Franxx'")
            else:
                if short_medium_long.lower() == "medium":
                    print("Recommendation: 'Attack on Titan'")
                else:
                    if short_medium_long.lower() == "long":
                        print("Recommendation: '7 Deadly Sins'")

else:
    if genre_choice.lower() == "romance":
        print("You have selected Romance")
        time = input("What year (2000s, 2010s): ")

        if time == "2000s":
            short_medium_long = input("How long should the manga be? (short, medium, long): ")

            if short_medium_long.lower() == "short":
                print("Recommendation: 'My Dress Up Darling'")
            else:
                if short_medium_long.lower() == "medium":
                    print("Recommendation: 'Maid Sama'")
                else:
                    if short_medium_long.lower() == "long":
                        print("Recommendation: 'Rent a Girlfriend'")

        else:
            if time == "2010s":
                short_medium_long = input("How long should the manga be? (short, medium, long): ")

                if short_medium_long.lower() == "short":
                    print("Recommendation: 'Rascal Does Not Dream Of Bunny Girl Senpai'")
                else:
                    if short_medium_long.lower() == "medium":
                        print("Recommendation: 'Ao Haru Ride (Blue Spring Ride)'")
                    else:
                        if short_medium_long.lower() == "long":
                            print("Recommendation: 'Dan Da Dan'")

    else:
        if genre_choice.lower() == "horror":
            print("You have selected Horror")
            time = input("What year (2000s, 2010s): ")

            if time == "2000s":
                short_medium_long = input("How long should the manga be? (short, medium, long): ")

                if short_medium_long.lower() == "short":
                    print("Recommendation: 'The Drifting Classroom'")
                else:
                    if short_medium_long.lower() == "medium":
                        print("Recommendation: 'Goth'")
                    else:
                        if short_medium_long.lower() == "long":
                            print("Recommendation: 'Hellsing'")

            else:
                if time == "2010s":
                    short_medium_long = input("How long should the manga be? (short, medium, long): ")

                    if short_medium_long.lower() == "short":
                        print("Recommendation: 'I Am a Hero'")
                    else:
                        if short_medium_long.lower() == "medium":
                            print("Recommendation: 'Ajin: Demi-Human'")
                        else:
                            if short_medium_long.lower() == "long":
                                print("Recommendation: 'Tokyo Ghoul'")
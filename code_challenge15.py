anime_list = []

while True:
    title = input("Enter the title of an anime or type 'exit' to finish: ").strip().lower()
    if title == 'exit':
        print("You have exited the anime entry program.")
        break
    else:
        anime_list.append(title)
        print(f"'{title}' has been added to the anime list.")

print("Your anime list includes:")
for anime in anime_list:
    print(f" - {anime}")

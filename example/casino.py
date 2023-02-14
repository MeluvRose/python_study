from random import randint

playing = True

while playing:
    pc_choice = randint(1, 50)

    print("Welcome to Guess Number game!!")
    user_choice = input(
        "Choose number(1 ~ 50, you want finish this game, typing 'x').\t"
    )
    if user_choice.upper() == "X":
        playing = False

    try:
        user_choice = int(user_choice)
        if user_choice == pc_choice:
            print("You Won!!!")
            playing = False
        elif user_choice > pc_choice:
            print(f"Lower! Computer choice {pc_choice}")
        else:
            print(f"Higher! Computer choice {pc_choice}")
    except:
        continue

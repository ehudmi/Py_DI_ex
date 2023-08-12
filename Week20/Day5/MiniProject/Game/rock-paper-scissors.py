from Game import Game

game_results = {"won": 0, "lost": 0, "draw": 0}


def get_user_menu_choice():
    print("Please select one of the following options")
    user_choice = input("(P)lay a new game or (S)how score or (Q)uit ").lower()
    return user_choice


def print_results(results):
    print("Thank you for playing")
    for k, v in results.items():
        print(f"You {k} {v} times")


def main():
    choice = get_user_menu_choice()
    while choice != "q":
        if choice == "p":
            new_game = Game()
            result = new_game.play()
            if result == "win":
                game_results["won"] += 1
            elif result == "lose":
                game_results["lost"] += 1
            else:
                game_results["draw"] += 1
            choice = get_user_menu_choice()
        elif choice == "s":
            print_results(game_results)
            choice = get_user_menu_choice()
        else:
            choice = get_user_menu_choice()
    if choice == "q":
        print_results(game_results)


main()

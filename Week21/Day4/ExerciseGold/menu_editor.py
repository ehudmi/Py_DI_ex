from menu_manager import MenuManager


def load_manager():
    return MenuManager()


def show_user_menu():
    menu = load_manager()
    while True:
        user_choice = input(
            """Menu
            (a) Add an item
            (b) Delete an item
            (v) View the menu
            (x) Exit
    """
        )
        if user_choice == "a":
            add_item_to_menu(menu)
        elif user_choice == "b":
            remove_item_from_menu(menu)
        elif user_choice == "v":
            show_restaurant_menu(menu)
        elif user_choice == "x":
            try:
                menu.save_to_file()
                print("new menu saved successfully")
            except:
                print("Goodbye")
            return False


def add_item_to_menu(menu):
    menu.add_item(
        input("What item would you like to add? ").capitalize(),
        int(input("What is the price of the item? ")),
    )


def remove_item_from_menu(menu):
    if menu.remove_item(input("What item would you like to remove? ").capitalize()):
        print("Them menu item was deleted successfully")
    else:
        print("it seems we had an error")


def show_restaurant_menu(menu):
    print(menu.menu)


show_user_menu()

from menu_manager import MenuManager
from menu_item import MenuItem


def show_user_menu():
    while True:
        user_choice = input(
            """Menu
            (V) View an item
            (A) Add an item
            (B) Delete an item
            (U) Update an item
            (S) Show the menu
            (X) Exit
    """
        )
        if user_choice == "v":
            show_item()
        elif user_choice == "a":
            add_item_to_menu()
        elif user_choice == "b":
            remove_item_from_menu()
        elif user_choice == "u":
            update_item_in_menu()
        elif user_choice == "s":
            show_restaurant_menu()
        elif user_choice == "x":
            print("Goodbye")
            return False


def show_item():
    print(
        MenuManager.get_by_name(
            input("What item would you like to view? ").capitalize()
        )
    )


def add_item_to_menu():
    menu = MenuItem(
        input("What item would you like to add? ").capitalize(),
        int(input("What is the price of the item? ")),
    )
    menu.save_item()


def remove_item_from_menu():
    menu = MenuItem(input("What item would you like to remove? ").capitalize(), 0)
    if menu.delete_item():
        print("Them menu item was deleted successfully")
    else:
        print("it seems we had an error")


def update_item_in_menu():
    menu = MenuItem(
        input("What item would you like to update? ").capitalize(),
        0,
    )
    menu.update_item(
        input("What is the new item name? ").capitalize(),
        int(input("What is the new item price? ")),
    )


def show_restaurant_menu():
    print(MenuManager.all_items())


show_user_menu()

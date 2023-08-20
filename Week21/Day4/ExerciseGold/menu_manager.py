import json


class MenuManager:
    def __init__(self) -> None:
        with open("./restaurant_menu.json", "r") as j_file:
            self.menu = json.load(j_file)

    def add_item(self, name, price):
        self.menu["items"].append({"name": name, "price": price})

    def remove_item(self, name):
        for i in range(0, len(self.menu["items"])):
            if self.menu["items"][i]["name"] == name:
                del self.menu["items"][i]
                return True

    def save_to_file(self):
        with open("./restaurant_menu.json", "w") as menu_file:
            json.dump(self.menu, menu_file, indent=2)

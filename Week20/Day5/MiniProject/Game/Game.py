from random import choice


class Game:
    def get_user_item(self):
        user_item = input("Choose (R)ock or (P)aper or (S)cissors ").lower()
        while user_item not in ["r", "p", "s"]:
            user_item = input("Choose (R)ock or (P)aper or (S)cissors ").lower()
        return user_item

    def get_computer_item(self):
        computer_item = choice(["r", "p", "s"])
        return computer_item

    def get_game_result(self, user_item, computer_item):
        if computer_item == user_item:
            return "draw"
        elif computer_item == "r" and user_item == "p":
            return "win"
        elif computer_item == "r" and user_item == "s":
            return "lose"
        elif computer_item == "p" and user_item == "s":
            return "win"
        elif computer_item == "p" and user_item == "r":
            return "lose"
        elif computer_item == "s" and user_item == "r":
            return "win"
        elif computer_item == "s" and user_item == "p":
            return "lose"

    def play(self):
        self.user_item = self.get_user_item()
        self.computer_item = self.get_computer_item()
        self.result = self.get_game_result(self.user_item, self.computer_item)
        if self.result == "draw":
            print(
                f"You selected {self.user_item}. The computer selected {self.computer_item}. You drew"
            )
        elif self.result == "win":
            print(
                f"You selected {self.user_item}. The computer selected {self.computer_item}. You won"
            )
        else:
            print(
                f"You selected {self.user_item}. The computer selected {self.computer_item}. You lost"
            )
        return self.result


# game_1 = Game()
# game_1.play()

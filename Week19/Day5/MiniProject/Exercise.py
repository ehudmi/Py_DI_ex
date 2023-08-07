# Create a TicTacToe game in python, where two users can play together.

# tic tac toe


# Instructions
# The game is played on a grid that’s 3 squares by 3 squares.
# Players take turns putting their marks (O or X) in empty squares.
# The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.
# When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.


# Hint
# To do this project, you basically need to create four functions:

# display_board() – To display the Tic Tac Toe board (GUI).
# player_input(player) – To get the position from the player.
# check_win() – To check whether there is a winner or not.
# play() – The main function, which calls all the functions created above.
# Note: The 4 functions above are just an example. You can implement many more helper functions or choose a completely
#  different approach if you want.


# Tips : Consider The Following:
# What functionality will need to occur every turn to make this program work?
# After contemplating the question above, think about splitting your code into smaller pieces (functions).
# Remember to follow the single responsibility principle! each function should do one thing and do it well!

BOARD = [
    [" ", " ", " ", "1", " ", " ", " ", "2", " ", " ", " ", "3", " ", " "],
    [" ", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
    ["1", "*", " ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " ", "*"],
    [" ", "*", "-", "-", "-", "|", "-", "-", "-", "|", "-", "-", "-", "*"],
    ["2", "*", " ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " ", "*"],
    [" ", "*", "-", "-", "-", "|", "-", "-", "-", "|", "-", "-", "-", "*"],
    ["3", "*", " ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " ", "*"],
    [" ", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
]


def display_board():
    for item in BOARD:
        print("".join(item))


def player_input(player, player_row, player_column):
    row = player_row * 2
    column = (player_column * 4) - 1
    if BOARD[row][column] == " ":
        BOARD[row][column] = player
    else:
        print("You cannot play this location")
    return (player, row, column)


def check_win(player, row, column):
    if BOARD[row].count(player) == 3:
        return True, player
    elif (
        BOARD[2][column] == player
        and BOARD[4][column] == player
        and BOARD[6][column] == player
    ):
        return True, player
    elif BOARD[2][3] == player and BOARD[4][7] == player and BOARD[6][11] == player:
        return True, player
    elif BOARD[6][3] == player and BOARD[4][7] == player and BOARD[2][11] == player:
        return True, player
    else:
        return False, player


def play():
    display_board()
    player = "X"
    win_flag = False
    print("Player X starts")
    while win_flag == False:
        print(f"Player {player}'s turn: ")
        player, row, column = player_input(
            player,
            int(input("Enter row ")),
            int(input("Enter column ")),
        )
        display_board()
        win_flag, player = check_win(player, row, column)
        if win_flag == True:
            break
        if player == "X":
            player = "O"
        else:
            player = "X"
    print(f"Player {player} - you won")


play()

board=[[4],
             [1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 3, 3, 3, 2, 3, 3, 3, 2, 3, 3, 3, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 3, 3, 3, 2, 3, 3, 3, 2, 3, 3, 3, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1],
             [4]
             ]
default=board.copy()

def play():
    player_turn=""
    win=False
    print("Hello, and Welcome to Tic-Tac-Toe!")
    while win is False:
        display()
        if check_win():
            print(f"Player {player_turn} Wins!!")
            return
        if player_turn=="X":
            player_turn="O"
        else:
            player_turn="X"
        [row,column]= player_input(player_turn)
        update_display(row,column, player_turn)

def display():
    line=17*"*"
    for row in default:
        for pixel in row:
            if pixel==4:
                print(line, end="")
            elif pixel==1:
                print("*", end="")
            elif pixel==2:
                print("|", end="")
            elif pixel==0:
                print(" ", end="")
            elif pixel==3:
                print("-", end="")
            elif pixel==5:
                print("X", end="")
            elif pixel==6:
                print("O", end="")
        print("")
def player_input(player_turn):
    print(f"Player {player_turn}'s Turn...")
    r=""
    c=""
    while r not in range(1,4):
        r=input("Enter a Row")
        try:
            r=int(r)
            if r not in range(1,4):
                raise ValueError
        except ValueError:
            print("Please enter a valid response!")
            r=0
    while c not in range(1,4):
        c=input("Enter a Column")
        try:
            c=int(c)
            if c not in range(1,4):
                raise ValueError
        except ValueError:
            print("Please enter a valid response!")
            c=0
    if check_sign(r, c):
        print("There is something there already!! Choose again!")
        [r,c]=player_input(player_turn)
    return [r,c]

def update_display(row, column, player_turn):
    if row==2:
        row=3
    elif row==3:
        row=5
    if column==1:
        column=3
    elif column==2:
        column=8
    else:
        column=13
    if player_turn=="X":
        default[row][column]=5
    else:
        default[row][column]=6

def check_win():
    win_rows=[1, 3, 5]
    win_columns=[3, 8, 13]
    checker=[]
    for row in win_rows:
        if default[row].count(5)==3 or default[row].count(6)==3:
            return True
    for diag in [1, -1]:
        for index, row in enumerate(win_rows):
            checker.append(default[row][diag*win_columns[index]])
        if checker.count(5)==3  or checker.count(6)==3:
            return True
        checker.clear()
    for column in win_columns:
        for row in win_rows:
            checker.append(default[row][column])
        if checker.count(5)==3  or checker.count(6)==3:
            return True
    return False
def check_sign(row, column):
    if row==2:
        row=3
    elif row==3:
        row=5
    if column==1:
        column=3
    elif column==2:
        column=8
    else:
        column=13
    if default[row][column]!=0:
        return True
    return False

play()
default=board.copy()

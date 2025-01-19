game_board = ["_", "_", "_",
              "_", "_", "_",
              "_", "_", "_"]

game_is_on = True
count = 0
char = "X"
inputs = []


def show_game():
    print("This is your Game board\n")
    print(f"{game_board[0]} | {game_board[1]} | {game_board[2]}      1|2|3\n")
    print(f"{game_board[3]} | {game_board[4]} | {game_board[5]}      4|5|6\n")
    print(f"{game_board[6]} | {game_board[7]} | {game_board[8]}      7|8|9\n")


def chance():
    global char
    if count % 2 == 0:
        char = "X"
    elif count % 2 != 0:
        char = "O"
    pos = input(f"Enter the number where you want to place your {char}: ")
    if pos in inputs:
        print("The position is occupied,Please give an Empty position")
        chance()
    inputs.append(pos)
    game_board[int(pos) - 1] = char


def cross_wins():
    global game_is_on
    print("The cross wins")
    game_is_on = False
    return game_is_on


def circle_wins():
    global game_is_on
    print("The Circle wins")
    game_is_on = False
    return game_is_on


def check():
    global game_is_on
    if game_board[0] == game_board[4] == game_board[8] == "X":
        cross_wins()
    elif game_board[0] == game_board[4] == game_board[8] == "O":
        circle_wins()
    elif game_board[0] == game_board[2] == game_board[1] == "X":
        cross_wins()
    elif game_board[0] == game_board[2] == game_board[1] == "O":
        circle_wins()
    elif game_board[3] == game_board[4] == game_board[5] == "X":
        cross_wins()
    elif game_board[3] == game_board[4] == game_board[5] == "O":
        circle_wins()
    elif game_board[6] == game_board[7] == game_board[8] == "X":
        cross_wins()
    elif game_board[6] == game_board[7] == game_board[8] == "O":
        circle_wins()
    elif game_board[0] == game_board[3] == game_board[6] == "X":
        cross_wins()
    elif game_board[0] == game_board[3] == game_board[6] == "O":
        circle_wins()
    elif game_board[1] == game_board[4] == game_board[7] == "X":
        cross_wins()
    elif game_board[1] == game_board[4] == game_board[7] == "O":
        circle_wins()
    elif game_board[2] == game_board[5] == game_board[8] == "X":
        cross_wins()
    elif game_board[2] == game_board[5] == game_board[8] == "O":
        circle_wins()


while game_is_on:
    count += 1
    show_game()
    chance()
    check()


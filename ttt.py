# 0 = nothing
# 1 = X
# 2 = O
import time

board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

# literally just change a value
# TODO: FIX
def input_value(value, row, column):
    if board[row][column] == 1 or board[row][column] == 2:
        print("Try again!")
        return False
    else:
        board[row][column] = int(value)
        return True


def print_board():

    # how much of a distance you want in between the numbers on the right side of the board and the actual board itself
    gap = 2
    # extra board
    converted_board = board.copy()

    # set up the board for printing (change numerical values into corresponding x or o)
    for i in range(len(converted_board)):
        for j in range(len(converted_board[i])):
            if converted_board[i][j] == 1:
                converted_board[i][j] = "X"
            elif converted_board[i][j] == 2:
                converted_board[i][j] = "O"

    # print the numbers on top of the board
    print(" "*(gap + 1) + "1 2 3")
    # print the numbers on the side of the board and then the actual board spaces after it
    for x in range(3):
        print(f"{x}" + " " * gap + str(converted_board[x]).replace("[", "").replace("]", "").replace(",", "").replace("'","").replace("0", "-"))

def get_input(turn):
    if turn == 1:
        answer = input("Enter Location X (\"row column\"):")
        return answer
    elif turn == 2:
        answer = input("Enter Location O (\"row column\"):")
        return answer

def check_game_state():
    # idk why i need this just weird bug with python maybe? definitely my fault but i don't know what causes it
    new_board = board.copy()
    for i in range(len(new_board)):
        for j in range(len(new_board[i])):
            if new_board[i][j] == "X":
                new_board[i][j] = 1
            if new_board[i][j] == "O":
                new_board[i][j] = 2

    # check for draws (when all spaces are filled)
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != 0:
                count+=1
    if count >= 9:
        return False, "Draw"

    # check for all wins
    for x in range(1, 3):
        for i in range(3):
            # columns
            if new_board[0][i] == x and new_board[1][i] == x and new_board[2][i] == x:
                return False, f"{x} Win"
            # rows
            if new_board[i][0] == x and new_board[i][1] == x and new_board[i][2] == x:
                return False, f"{x} Win"
        # diagonals
        if new_board[1][1] == x:
            if new_board[0][0] == x and new_board[2][2] == x:
                return False, f"{x} Win"
            if new_board[0][2] == x and new_board[2][0] == x:
                return False, f"{x} Win"

    # else
    return True, "Continue"


def start_game():
    input("TTT! Enter to continue")

    turn = int(input("Who goes first? 1 for X, 2 for O\n"))
    time.sleep(0.3)

    turn_valid = True
    while check_game_state()[0]:
        print_board()
        answer = get_input(int(turn)).replace(" ", "")
        row = int(answer[0]) - 1
        column = int(answer[1]) - 1
        input_value(turn, row, column)

        # switch turns
        if turn == 1:
            turn = 2
        else:
            turn = 1

    print_board()
    ending = check_game_state()[1]
    match ending:
        case "Draw":
            print("Draw! All spaces filled.")
        case "1 Win":
            print("X Wins!")
        case "2 Win":
            print("O Wins!")

start_game()
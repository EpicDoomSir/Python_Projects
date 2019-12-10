"""making tic tac toe"""

VICTORY_MESSAGE = "You Win!!"
TRY_AGAIN_MESSAGE = "again"


def make_board():
    boxes = [
        [" "] * 3,
        [" "] * 3,
        [" "] * 3
    ]
    return boxes


def play_on_board(boxes, piece, placement):
    x_coordinate = placement[0] - 1
    y_coordinate = placement[1] - 1
    boxes[x_coordinate][y_coordinate] = piece
    display_board(boxes)


def display_board(boxes):
    column = ['']
    for i in range(3):
        for j in range(3):
            column += boxes[i][j]
            if j != 2:
                column += "|"
        if i != 2:
            column += "\n" + "~"*5 + "\n"
    print(' '.join(column))
    # print(f" {boxes[0][0]} " + "|" + f" {boxes[0][1]} " + "|" + f" {boxes[0][2]} ")
    # print("~" * 11)
    # print(f" {boxes[1][0]} " + "|" + f" {boxes[1][1]} " + "|" + f" {boxes[1][2]} ")
    # print("~" * 11)
    # print(f" {boxes[2][0]} " + "|" + f" {boxes[2][1]} " + "|" + f" {boxes[2][2]} ")


def player_input():
    verify = False
    while not verify:
        play = input("Your turn, what piece are you using? x/o ")
        if play not in ('x', 'o'):
            pass
        else:
            verify = True
    return play


def player_position():
    global unparsed_coordinates
    verify = False
    while not verify:
        position = input("choose where you want to place your piece. Ex. 1,2 = row 1 column 2 ")
        unparsed_coordinates = position.split(",")
        if len(unparsed_coordinates) != 2:
            pass
        else:
            verify = True
    return tuple(map(int, unparsed_coordinates))


def win_check(board):
    if win_horizontal(board) == VICTORY_MESSAGE or win_vertical(board) == VICTORY_MESSAGE or win_diagonal(board) == VICTORY_MESSAGE:
        print(VICTORY_MESSAGE)
    else:
        return TRY_AGAIN_MESSAGE


def win_horizontal(board):
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][1] != " ":
            return VICTORY_MESSAGE
    else:
        return TRY_AGAIN_MESSAGE


def win_vertical(board):
    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[1][i] != " ":
            return VICTORY_MESSAGE
    else:
        return TRY_AGAIN_MESSAGE


def win_diagonal(board):
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] != " ":
        return VICTORY_MESSAGE
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1] != " ":
        return VICTORY_MESSAGE
    else:
        return TRY_AGAIN_MESSAGE


def main():
    board = make_board()
    display_board(board)
    while win_check(board) == TRY_AGAIN_MESSAGE:
        play_on_board(board, player_input(), player_position())


if __name__ == '__main__':
    main()

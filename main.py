# tic tac toe Game

# init board
board = ['-'] * 10

# show current board
def show_board():
    print(f'{board[7]} | {board[8]} | {board[9]}')
    print(f'{board[4]} | {board[5]} | {board[6]}')
    print(f'{board[1]} | {board[2]} | {board[3]}')
    # board[0] will never use , just define for being easy to read code
    return

# select move
def select_action():
    pass

# move as player select and mark
def move():
    pass


# flip player mark between X and O
def flip_player():
    pass

def check_game_is_over():

    def check_rows():
        pass


    def check_coulmns():
        pass


    def check_diagonals():
        pass


# main function that run at the end
def main():
    show_board()

main()

# tic tac toe Game


# glob variables
winner = None
game_is_over = False
p1 = None
p2 = None
player_turn = None



# init board
board = ['-'] * 10


# show current board
def show_board():
    print(f'{board[7]} | {board[8]} | {board[9]}')
    print(f'{board[4]} | {board[5]} | {board[6]}')
    print(f'{board[1]} | {board[2]} | {board[3]}')
    # board[0] will never use , just define for being easy to read code
    return


# select player marker as X adn O in order p1 and p2(p = player)
def player_marker():
    global p1, p2, player_turn

    while p1 not in ['X', 'O']:
        p1 = input('p1 select between X and O : ')

    if p1 == 'X':
        p2 = 'O'
    else:
        p2 = 'X'

    player_turn = p1

    print(f'p1 : {p1}, p2 : {p2}')

# announce player's turn
def announce_turn():
    print(f'{player_turn}\' turn')
    return

# select move
def select_action():
    player_select = None

    allowed_choice = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    while True:
        player_select = input('select from 1-9: ')

        if player_select not in allowed_choice:
            print('notallowed action, try again !')
            continue

        if board[int(player_select)] in ['X', 'O']:
            print(f'this cell selected by {board[int(player_select)]} before')
            continue

        break
    return int(player_select)


# move as player select and mark
def move():

    action = select_action()
    board[action] = player_turn
    return


# flip player mark between X and O
def flip_player():
    global player_turn

    if player_turn == p1:
        player_turn = p2
    else:
        player_turn = p1
    return


def check_game_is_over():

    def check_rows():
        pass

    def check_coulmns():
        pass

    def check_diagonals():
        pass

    def check_draw():
        empty_count = 0
        for cell in board:
            if cell not in ['X', 'O']:
                empty_count += 1

        return empty_count == 1


    if check_draw():
        global game_is_over
        game_is_over = True

def announce_winne(our_winner):
    if our_winner == p1:
        print(f'p1 win as {p1}')
    elif our_winner == p2:
        print(f'p2 win as {p2}')
    else:
        print('draw . . .')


# main function that run at the end
def main():

    show_board()
    player_marker()

    while not game_is_over:
        show_board()
        announce_turn()
        move()
        flip_player()
        check_game_is_over()

    announce_winne(winner)

main()

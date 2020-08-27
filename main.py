# tic tac toe Game

#import os for system function
import os

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


# if none of them gona true, game will be continue
def check_game_is_over():

    global game_is_over
    global winner


    # Check Each Row
    def check_rows():
        row_3 = board[7] == board[8] == board[9] in ['X', 'O']
        row_2 = board[4] == board[5] == board[6] in ['X', 'O']
        row_1 = board[1] == board[2] == board[3] in ['X', 'O']

        if row_1 or row_2 or row_3:
            return True

    if check_rows():

        game_is_over = True
        winner = player_turn
        return

    # Check Each Coulmns
    def check_coulmns():
        col_1 = board[1] == board[4] == board[7] in ['X', 'O']
        col_2 = board[2] == board[5] == board[8] in ['X', 'O']
        col_3 = board[3] == board[6] == board[9] in ['X', 'O']

        if col_1 or col_2 or col_3:
            return True

    if check_coulmns():

        game_is_over = True
        winner = player_turn
        return

    # Check Each Diagonal
    def check_diagonals():
        diagonal_1 = board[1] == board[5] == board[9] in ['X', 'O']
        diagonal_2 = board[3] == board[5] == board[7] in ['X', 'O']

        if diagonal_1 or diagonal_2:
            return True

    if check_diagonals():

        game_is_over = True
        winner = player_turn
        return

    # Check For Tie
    def check_draw():
        empty_count = 0
        for cell in board:
            if cell not in ['X', 'O']:
                empty_count += 1

        return empty_count == 1


    if check_draw():

        game_is_over = True
        return


# announce winner after game is game_is_over(No wiiner => Tie or Draw)
def announce_winner(our_winner):
    if our_winner == p2:
        print(f'p1 win as {p1}')
    elif our_winner == p1:
        print(f'p2 win as {p2}')
    else:
        print('draw ...')


# clear outpu each stage
def clear():
    os.system('clear')


# main function that run at the end
def main():

    clear()
    show_board()
    player_marker()
    clear()

    while not game_is_over:
        show_board()
        announce_turn()
        move()
        clear()
        flip_player()
        check_game_is_over()

    show_board()
    announce_winner(winner)


# Run Game
main()

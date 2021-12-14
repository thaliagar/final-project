import random


def print_board(board):
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])


def choose_player_letter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Choose your letter: X or O ')
        letter = input().upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def rand_first_turn():
    if random.randint(0, 1) == 0:
        return 'player'
    else:
        return 'computer'


def get_player_move(): # returns valid player move
    while True:
        space = int(input())
        if space == 1 or space == 2 or space == 3 or space == 4 or space == 5 or space == 6 or space == 7 or space == 8 or space == 9:
            break

    return space


def is_space_free(board, move):
    # returns true if move is free given the board
    return board[move] == ''


def is_board_full(board):
    # only returns true if every space is taken
    for i in range(0, 9):
        if is_space_free(board, i):
            return False
    return True


def check_win(board): # checks horizontals, verticals, & diagonals for wins
    if board[0] == board[3] == board[6] and board[0] != '':
        return True, board[0]

    if board[1] == board[4] == board[7] and board[1] != '':
        return True, board[1]

    if board[2] == board[5] == board[8] and board[2] != '':
        return True, board[2]

    if board[0] == board[1] == board[2] and board[0] != '':
        return True, board[0]

    if board[3] == board[4] == board[5] and board[3] != '':
        return True, board[3]

    if board[6] == board[7] == board[8] and board[6] != '':
        return True, board[6]

    if board[0] == board[4] == board[8] and board[0] != '':
        return True, board[0]

    if board[2] == board[4] == board[6] and board[2] != '':
        return True, board[2]

    return False, ''


def make_computer_move(board): # computer checks possible moves, blocks wins, + plays randomly
    for i in range(len(board)):
        if is_space_free(board, i):
            current_letter = board[i]
            board[i] = 'X'
            win_state, player = check_win(board)
            if win_state:
                return i
            board[i] = current_letter

    for i in range(len(board)):
        if is_space_free(board, i):
            current_letter = board[i]
            board[i] = 'O'
            win_state, player = check_win(board)
            if win_state:
                return i
            board[i] = current_letter

    while True:
        computer_move = random.randint(0, 8)
        if is_space_free(board, computer_move):
            return computer_move


def play_tictactoe():
    board = [''] * 9
    player_letter, computer_letter = choose_player_letter()
    turn = rand_first_turn()
    print('The ' + turn + ' will go first')
    print_board(board)

    while True:
        if turn == 'player':
            while True:
                print('choose a space')
                chosen_space = get_player_move() - 1
                if is_space_free(board, chosen_space):
                    break
            board[chosen_space] = player_letter
            print('after player move')
            print_board(board)
            win_state, winning_player = check_win(board)
            if win_state:
                print('PLAYER WINS!')
                return 0
            if is_board_full(board):
                print('DRAW')
                return 0
            turn = 'computer'

        if turn == 'computer':
            chosen_space = make_computer_move(board)
            print('board after computer move: ')
            board[chosen_space] = computer_letter
            print_board(board)
            win_state, winning_player = check_win(board)
            if win_state:
                print('COMPUTER WINS!')
                return 0
            if is_board_full(board):
                print('DRAW')
                return 0
            turn = 'player'


play_tictactoe()

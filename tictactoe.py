import random

BOXES = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ]
WIN_COMBOS = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
              [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6], ]

EXAMPLE_BOARD = (('''
    {0} | {1} | {2}
    ---------------
    {3} | {4} | {5}
    ---------------
    {6} | {7} | {8}
            '''))


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


def make_move(board, letter, move):
    board[move] = letter

def is_winner(board):
    # checks board for WIN_COMBOS
    # checks next move for wins?


def is_space_free(board, move):
    # returns true if move is free given the board
    return board[move] == ''


def is_board_full(board):
    # only returns true if every space is taken
    for i in range(0, 9):
        if is_space_free(board, i):
            return False
        return True


def play_tictactoe():
    # while game is playing
     print_board(board)


# main program

print('welcome to tic tac toe: you vs. computer! \n')
print('here is how the board is set up: each number corresponds to a position on the board \n')
print(EXAMPLE_BOARD)
play_tictactoe()

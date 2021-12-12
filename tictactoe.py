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


def print_board(initial=False):
    print(('''
    {} | {} | {}
    -------------
    {} | {} | {}
    -------------
    {} | {} | {}
            ''').format(*([x for x in range(1, 10)] if initial else BOXES)))


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


def play_tictactoe():
    while True:
        initial_board = [''] * 10
        player_letter, computer_letter = choose_player_letter()
        turn = rand_first_turn()
        print('The' + turn + 'will go first')
        is_playing = True

    while is_playing:
        if turn == 'player'
            print_board(initial_board)


# main program
print('welcome to tic tac toe: you vs. computer! \n')
print('here is how the board is set up: each number corresponds to a position on the board \n')
print(EXAMPLE_BOARD)
play_tictactoe()

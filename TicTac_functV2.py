# this version includes multiplayer and AI
# the AI in this version is just a dummy AI see smarter implementation in the OOP version 

import random

board = ['-' for i in range(9)]
#  list comprehension was just used to print board, '_' can be input manually if reader doesnt understand list-com

# a single list comprehension can be used for the display board .. see OOP version
def display_board():
    print(" | ".join(board[0:3]))
    print(" | ".join(board[3:6]))
    print(" | ".join(board[6:9]))

#  this commented block below would work perfectly inplace of the three-lines above .. i.e DRY

    # for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:
    #     print(' | '.join(row))

def check_win():
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]  # diagonals
    ]
    for p in ['x', 'o']:
        for condition in win_conditions:
            if all(board[i] == p for i in condition):
                return True

    return False
# create computer input function
def human_input():
    while True:
        try:
            v = int(input('Enter position: '))
            if 1 <= v <= 9:      # you can also use if v in range(1, 10)
                if board[v - 1] == '-':
                    return v
                else:
                    print('Enter another value, value already exists')
            else:
                print('Enter a value between 1 and 9')
        except ValueError:
            print('Please enter a number')

# the ai block need no try and except since it choices are constrained
def ai_input():
    while True:
        v = random.randrange(1, 10)
        if board[v - 1] == '-':
            return v
        else:
            print('Enter another value, value already exists')


# if mode is not , input only one player name
display_board()  # this call here is not necessary
print('welcome to tic tac toe ')


def play_mode():
    mode = input('pls enter game mode, m for multiplayer or c to play with AI: ').upper()
    while mode not in ['M', 'C']:
        mode = input('pls enter game mode, m for multiplayer or c to paly with AI: ').upper()
    return mode

game_type = play_mode()

if game_type == 'M':
    player1 = input('Enter player1 name: ')
    player2 = input('Enter player2 name: ')

# didn't intentionally use an elif here since the output from calling Play_mode() can only be either M or C
else:
    player1 = input('Enter player1 name: ')
    player2 = 'AI'


while True:

    for i in range(9):
        if i % 2 == 0:
            player = player1
            p = 'x'
            display_board()
        else:
            player = player2
            p = 'o'
            display_board()
        print(f'{player} turn')
        # define mode here based on selection
        if game_type == 'M':
            v = human_input()  # any other variable name can be used in place of v here
            board[v - 1] = p

        else:  # this else block just switches turns btw human and computer
            if i % 2 == 0:
                v = human_input()
                board[v - 1] = p
            else:
                v = ai_input()
                board[v - 1] = p

        if check_win():
            display_board()
            print(f'{player} wins!')
            break
    else:
        print("It's a draw!")
        display_board()  # want board to be displayed here in case of draw

    # add a function here to reset mode or continue playing in present state

    if input("Do you want to play again? (y/n) ") == 'n':
        break
    else:
        print('new round')
        board = ['-' for e in board]


# TODO: features to add ..... counting of scores and updating it..
#  train AI to play better ...
#  also add a main block and switching play mode
#  for multiplayer add switching of turn of who plays first ..after each mode
print('this is a new line')
print('another line')
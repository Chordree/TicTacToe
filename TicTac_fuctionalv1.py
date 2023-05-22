# this version is for multiplayer alone ..see other version for combination with AI

board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-'
         ]


# board = ['-' for i in range(9)]
#  this listcomp can also work as the board variable above

def display_board():
    print(" | ".join(board[0:3]))
    print(" | ".join(board[3:6]))
    print(" | ".join(board[6:9]))


#  look for how to make this line above more concise ..i.e DRY

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

def inp():
    while True:
        try:
            v = int(input('Enter position: '))
            if 1 <= v <= 9:
                if board[v - 1] == '-':
                    return v
                else:
                    print('Enter another value, value already exists')
            else:
                print('Enter a value between 1 and 9')
        except ValueError:
            print('Please enter a number')


display_board()  # this call here is not necessary
print('welcome to tic tac toe ')
player1 = input('Enter player1 name: ')
player2 = input('Enter player2 name: ')

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
        v = inp()  # any other variable name can be used in place of v here
        board[v - 1] = p
        if check_win():
            display_board()
            print(f'{player} wins!')
            break
    else:
        print("It's a draw!")

    if input("Do you want to play again? (y/n) ") == 'n':
        break
    else:
        print('new round')
        board = ['-' for e in board]


# TODO: features to add ..... counting of scores and updating it..
#  play with AI .. see implementation in version 2
#  can add rules later on for user to choose type of rules

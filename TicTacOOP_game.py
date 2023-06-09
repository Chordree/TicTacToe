from player_oop import HumanPlayer, AiPlayer
class TicTac:
    def __init__(self):
        self.board = ['_' for i in range(9)]
        self.current_winner = None  # this keeps track of winning state after every move

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('|'.join(row))  # remove the straight lines by the side they are just for the edges

    # check what static methods do.. noticed it doesnt take self variable
    @staticmethod
    def print_board_nums():
        num_board = [[str(i+1) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in num_board:
            print('|'.join(row))

    def available_moves(self):
        # moves = moves = [ i  for (i,spot) in enumerate(self.board) if spot == '_']
        # this list com above can replace the whole block of code in this function
        moves = []
        for (i, spot) in enumerate(self.board):
            if spot == '_':
                moves.append(i)
        return moves
# check the major diff btw this functions above and below this line
    # think the one below returns a boolean True if there is still an empty port
    # change the port to spot later on
    def empty_slots(self):
        return '_' in self.board

    def len_empty_spots(self):
        return len(self.available_moves())
        #  or return self.board.count('_') will also work inplace of the above

    # see if this should be renamed to get_move compare with get_move in the player module
    def make_move(self, position, letter):
        if self.board[position] == '_':
            self.board[position] = letter
            if self.winner(position, letter):
                self.current_winner = letter
            return True
        return False
# check the maths and the logic behind this winning conditions
    def winner(self, pos, letter):
        row_index = pos // 3
        row = self.board[row_index*3: (row_index+1)*3]
        if all([spot == letter for spot in row]):
            return True
        col_index = pos % 3
        col = [self.board[col_index + (i*3)] for i in range(3)]
        if all([spot == letter for spot in col]):
            return True

        if pos % 2 == 0:
            diag1 = [self.board[i] for i in [0, 4, 8]]
            diag2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diag1]) or all([spot == letter for spot in diag2]):
                return True
        return False

def play(game, x_player, o_player, print_game=True):
# note print_game was intentionally added can be switched off in time of multiple simulations
    if print_game:
        game.print_board_nums()
        #  this function was only used once to show port numbers of different positions

    letter = 'x'  # starting letter ..see to this later

    while game.empty_slots():
        if letter == 'o':
            choice = o_player.get_move(game)  # see how the .get_move(game) method works here
        elif letter == 'x':
            choice = x_player.get_move(game)

        # include function to add player name instead of playerx and player o"s turn
        # see wether a fuction is automatically set to true
        if game.make_move(choice, letter):  # see why the if make_move is working there
            if print_game:
                print(letter, f'places his game in port {choice +1}')
                game.print_board()
                print()

            if game.current_winner:
                if print_game:
                    print(f'player {letter} has won the game')
                return letter


        # see how this works
        letter = 'o' if letter == 'x' else 'x'
        #  # same as the below
        # if letter == 'x':
        #     letter = 'o'
        # else:
        #     letter = 'x'

    # i.e the code only gets here if all spaces are filled
#  i.e the true value, game.empty_slots() for the while loop becomes false
    if print_game:
         print('it is a tie ')

# add some more functionalities to switch playmode and continue playing, during tie and quiting when done
def set_mode():
    mode = input('pls enter game mode, m for multiplayer or c to play with AI: ').upper()
    while mode not in ['M', 'C']:
        mode = input('pls enter game mode, m for multiplayer or c to paly with AI: ').upper()
    return mode
game_type =  initial_game_type = set_mode()

def main(game_type):


    # to allow player to choose if playing with computer or multiplayer
    if game_type == 'M':
        x_player = HumanPlayer('x')
        o_player = HumanPlayer('o')
    else:
        x_player = HumanPlayer('x')
        o_player = AiPlayer('o')
    
    t = TicTac()
    play(t, x_player, o_player)  # note print_game  uses its default val since it wasnt specified 

    while True:
        replay = input('enter [y] to continue same mode, [q] to quit,  any [other key] to change mode: ').upper()
        # the upper method above was just used to handle case sensitivity
        if replay == 'Y':
            main(game_type)
        elif replay != 'Q':
            game_type = set_mode()
            main(game_type)
        break

# Todo: add player names .. and set mode to not start entirely from the play mode
#  add time.sleep effect so computer doesnt just play immediately
if __name__ == '__main__':
    main(game_type)



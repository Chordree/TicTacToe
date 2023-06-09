import math
import random


# this is not really necessary just used it to show how inheritance works 
class Player:
    def __init__(self, letter):
        self.letter = letter


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # the suggestion below worked perfectly well .. use while true and break
        valid_choice = False  # see to changing this to true .. no not in while condition ..the false in loop
        val = None  # see if setting val to none here is necessary
        # look for a better way to set this while loop condition
        while not valid_choice:
            choice = input(self.letter + "'s turn. input move(1 -9): ")
            try:
                val = int(choice) - 1  # this has handled the +1 effect in the position
                if val not in game.available_moves():
                    raise ValueError
                valid_choice = True
            except ValueError:
                print('invalid input pls, check and try again')
        return val


class AiPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        choice = random.choice(game.available_moves())
        # see how the method game.available_moves() is taking effect
        return choice


# TODO: complete this unbeatable AI using minimax algorithm
class SuperAiPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    # check major diff btw this and the make_move in the game
    def get_move(self, game):
        if len(game.available_moves()) == 9:
            choice = random.choice(game.available_moves())
        else:
            choice = self.minimax(game, self.letter)['position']
        return choice

    # Todo : add and unbeatble Ai using minimax algorithm 
# Problem Statement :

# Basic Board: On a board (Of size 100), for a dice throw a player should
# move from the initial position by the number on dice throw.

# Add a snake on the board: A snake moves a player from its start position to end position. where start position > end position
# Test data: Add a snake at position 14 moving the player
# to position 7.

# Make A Crooked Dice: A dice that only throws Even numbers.
# The can game can be started with normal dice or crooked dice.

import math
import random
class Dice:
    def __init__(self, Type):
        self.Type = Type

    def roll(self):
        if self.Type == "Normal":
            return random.choice([2, 4, 6])
        else:
            return random.choice([1,2,3,4,5,6])
start = 14
end = 7

dice = Dice("Normal")

dice.roll()


#chat GPT

import random

# Define a class for the game board
class GameBoard:
    def __init__(self, size=100):
        self.size = size
        self.board = [0] * (size + 1)  # Initialize the board with positions
        
    def add_snake(self, start, end):
        # Add a snake to the board
        if start > end and 0 < start <= self.size and 0 < end <= self.size:
            self.board[start] = end
            
    def move_player(self, player, steps):
        # Move the player on the board
        if 0 < player <= self.size:
            new_position = player + steps
            if new_position <= self.size:
                if self.board[new_position] != 0:
                    # The player has encountered a snake
                    new_position = self.board[new_position]
                player = new_position
        return player


# Define a class for the crooked dice
class CrookedDice:
    def roll(self):
        # Roll the crooked dice (even numbers only)
        return random.choice([2, 4, 6])


# Define a class for the normal dice
class NormalDice:
    def roll(self):
        # Roll the normal dice (any number between 1 and 6)
        return random.randint(1, 6)


# Define a class for the game
class SnakeAndLadderGame:
    def __init__(self):
        self.board = GameBoard()
        self.dice = None
        self.current_player_position = 0

    def set_dice(self, is_crooked):
        # Set the type of dice for the game (crooked or normal)
        if is_crooked:
            self.dice = CrookedDice()
        else:
            self.dice = NormalDice()

    def play_turn(self):
        # Simulate a player's turn
        dice_roll = self.dice.roll()
        print(f"Player rolled a {dice_roll}")
        self.current_player_position = self.board.move_player(self.current_player_position, dice_roll)
        print(f"Player is now at position {self.current_player_position}")


# Example usage:
if __name__ == "__main__":
    game = SnakeAndLadderGame()
    game.board.add_snake(14, 7)  # Add a snake from position 14 to 7
    game.set_dice(is_crooked=True)  # Use a crooked dice
    game.play_turn()

# This is the main file for the Rock-Paper-Scissors game. It imports the necessary modules and runs the game.

from RPS_game import play, quincy, mrugesh, kris, abbey, human, random_player
from RPS import player
from unittest import main

#play(player, quincy, 1000)
#play(player, abbey, 1000)
#play(player, kris, 1000)
#play(player, mrugesh, 1000)



# Uncomment line below to play interactively against a bot:
play(human, abbey, 20, verbose=True)

# Uncomment line below to play against a bot that plays randomly:
# play(human, random_player, 1000)



# Uncomment line below to run unit tests automatically
main(module='test_module', exit=False)
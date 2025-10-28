# My base game - Main file
# Start date: 27, 10, 2025
# By: Lewis Burt
''' This is the main executable in python. '''

# Imports:
# modules:
# import sys
# from os import path
# # My files:
import Python_Files.game as GAME

game = GAME.Game()

game.show_start_screen()
while game.running:
    game.new_game()
    game.show_gameover_screen()

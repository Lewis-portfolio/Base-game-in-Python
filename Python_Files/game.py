# My base game - Game class
# Start date: 27, 10, 2025
# By: Lewis Burt
''' This is the main Class in python. '''

# Imports:
import sys
import pygame as PG


WIDTH = 1024
HEIGHT = 768


class Game():
    ''' The class responsible for the game to run. '''
    def __init__(self):
        PG.mixer.pre_init(44100, -16, 2, 2048)
        # Initialise the game window:
        PG.init()
        PG.mixer.init()
        self.screen = PG.display.set_mode((WIDTH, HEIGHT))  # hello
        PG.display.set_caption("Base Game")

        # Preparation for updates:
        self.clock = PG.time.Clock()
        PG.key.set_repeat(500, 100)
        self.running = True

        # To load data:

    def get_level(self):
        ''' Get's the current level of the game'''

    def new_game(self):
        ''' Starts a new game. '''

    def get_groups(self):
        ''' Get's the groups of a game. '''

    def run_game(self):
        ''' Runs the game. '''

    def game_events(self):
        ''' The events of a game. '''

    def game_updates(self):
        ''' The update events for the game. '''

    def game_draw(self):
        ''' The draw events of the game. '''

    def show_start_screen(self):
        ''' Shows a start screen. '''

    def show_gameover_screen(self):
        ''' Shows a game over screen. '''

    def quit_game(self):
        ''' Quits the game. '''
        PG.quit()
        sys.exit()

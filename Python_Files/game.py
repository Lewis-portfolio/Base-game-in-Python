# My base game - Game class
# Start date: 27, 10, 2025
# By: Lewis Burt
''' This is the main Class in python. '''

# Imports:
import sys
from os import path
import pygame as PG
import settings
from python_files import maps
from python_files.loaders import map_class



WIDTH = 1024
HEIGHT = 768


class Game():
    """ The class responsible for the game to run. """
    def __init__(self, game_exe):
        PG.mixer.pre_init(44100, -16, 2, 2048)
        # Initialise the game window:
        PG.init()
        PG.mixer.init()
        self.screen = PG.display.set_mode((WIDTH, HEIGHT))
        PG.display.set_caption("Base Game")
        #------------------------------------------------#
        # Preparation for updates:
        self.clock = PG.time.Clock()
        PG.key.set_repeat(500, 100)
        self.running = True
        self.dt = None  # Delta time
        self.is_paused = False
        #self.font_name = PG.font.match_font(font_name)
        # To load data:
        self.groups = {}
        self.maps = {}
        self.c_map = None
        # Loading data:
        self.game_folder = path.dirname(game_exe)
        self.load_maps()
        self.get_level()


    def load_maps(self):
        """ Loads the map names. """
        for basic_map in maps.basic_maps:
            self.maps[basic_map[:-4]] = basic_map

    def get_level(self, selection="basic_map"):
        """ Get's the current level of the game"""
        if selection not in ["basic"]:
            self.c_map = map_class.MapClass(self.maps["basic_map"])


    def new_game(self):
        """ Starts a new game. """
        self.load_maps()
        # self.get_level()
        self.get_groups()
        # Temporary to be removed:
        print(f" Game - new_game: {self.maps}")
        self.run_game()


    def get_groups(self):
        """ Get's the groups of a game. """
        all_sprites = PG.sprite.LayeredUpdates()
        self.groups["all_sprites"] = all_sprites
        for group in ["walls", "mobs", "bullets", "items"]:
            self.groups[group] = PG.sprite.Group()
            print(f" Game - get_groups: {group}")

    def run_game(self):
        """ Runs the game. """
        while self.running:
            self.dt = self.clock.tick(settings.FPS) / 1000
            self.game_events()
            if not self.is_paused:
                self.game_updates()
            self.game_draw()

    def game_events(self):
        """ The events of a game. """

    def game_updates(self):
        """ The update events for the game. """

    def game_draw(self):
        """ The draw events of the game. """

    def show_start_screen(self):
        """ Shows a start screen. """

    def show_gameover_screen(self):
        """ Shows a game over screen. """

    def quit_game(self):
        """ Quits the game. """
        PG.quit()
        sys.exit()

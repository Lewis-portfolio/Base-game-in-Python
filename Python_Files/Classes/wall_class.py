# My base game - Wall class
# Start date: 05, 11, 2025
# By: Lewis Burt
''' This is the wall Class in python. '''

# Imports:
import pygame as PG
from base_sprite_class import BaseObjectClass

class ObstacleClass(BaseObjectClass):
    """ A class for walls. """
    def __init__(self, game, pos, w, h):
        self.group = game.groups["walls"]
        super().__init__(game, self.group, pos, w, h)

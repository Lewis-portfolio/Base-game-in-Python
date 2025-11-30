# My base game - Base sprite class
# Start date: 05, 11, 2025
# By: Lewis Burt
''' This is the Base Class for my game in python. '''

# Imports:
import pygame as PG


class BaseObjectClass(PG.sprite.Sprite):
    """ The basics of every object in the game. """
    def __init__(self, game, groups, pos, dimensions = (32, 32)):
        self.groups = groups
        PG.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = PG.Rect((pos), dimensions)
        self.pos = pos
        self.rect.x , self.rect.y = pos

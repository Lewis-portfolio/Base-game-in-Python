# Start date: 23, 11, 2025
# By: Lewis Burt
''' This is the map classes for the base game. '''

# Imports:
# from os import path
import pygame as PG
import pytmx as PT
from python_files import settings

# To be moved:
TILE_SIZE = 32


class MapClass():
    """ The map class to make a map using a file. """
    def __init__(self, file_name):
        self.data = []
        if file_name[:-4] == ".tmx":
            self.tiled_map(file_name)
        elif file_name[:-4] == ".txt":
            self.basic_map(file_name)


    def tiled_map(self, file_name):
        """ Makes a tiled map. """
        tm = PT.load_pygame(file_name, pixelalpha= True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmx_data = tm


    def render_tiled_map(self, surface):
        """ renders the tiled map. """
        ti = self.tmx_data.get_tile_image_by_gid
        for layer in self.tmx_data.visible_layers:
            if isinstance(layer, PT.TiledTileLayer):
                for x, y, gid in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile,
                                    (x * self.tmx_data.tilewidth,
                                    y * self.tmx_data.tileheight))


    def make_tiled_map(self):
        """ Makes the tiled map surfaces. """
        temp_surface = PG.Surface((self.width, self.height))
        self.render_tiled_map(temp_surface)
        return temp_surface


    def basic_map(self, file_name):
        """ Makes a basic map. """
        self.data = []
        with open(file_name, "rt", encoding="utf-8") as file:
            for line in file:
                self.data.append(line.strip())
        self.tile_width = len(self.data[0])
        self.tile_height = len(self.data)
        self.width = self.tile_width * TILE_SIZE
        self.height = self.tile_height * TILE_SIZE


class CameraClass():
    """ The camera class for my game. """
    def __init__(self, width, height):
        self.cam = PG.Rect(0, 0, width, height)
        self.width = width
        self.height = height


    def act_apply(self, entity):
        """ moves an entity relative to camera movements. """
        return entity.rect.move(self.cam.topleft)


    def act_apply_rect(self, rect):
        """ moves a rect relative to camera movements. """
        return rect.move(self.cam.topleft)


    def update(self, target):
        """ Follows the player character. """
        x = - target.rect.centerx + int(settings.WIDTH / 2)
        y = - target.rect.centery + int(settings.HEIGHT / 2)

        # Limits the movement to the size of the map:
        x = min(0, x)
        y = min(0, y)
        x = max(-(self.width - settings.WIDTH), x) # Limit Right
        y = max(-(self.height - settings.HEIGHT), y) # Limit Bottom
        self.cam = PG.Rect(x, y, self.width, self.height)

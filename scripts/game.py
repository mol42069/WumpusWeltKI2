import pygame as pg
import random as rnd
from enum import Enum

class Field:
    def __init__(self, pos, field_sprite):
        self.pos = pos
        self.sprite = field_sprite
        if rnd.randint(0, 4) == 0:          # there is a 20% chance that a field is a pit
            self.pit = True
        else:
            self.pit = False

        if pos == [0, 0]:                   # we know that field [0, 0] is the player spawn
            self.player = True
        else:
            self.player = False
        self.breeze = False
        self.stench = False
        self.wumpus = False
        self.gold = False

class Sprites(Enum):
    empty = 0
    wumpus = 1
    gold = 2
    pit = 3
    stench = 4
    breeze = 5
    player = 6


def load_sprites():
    sprites = [
                pg.image.load('./resources/empty_field.png'),
                pg.image.load('./resources/wumpus.png'),
                pg.image.load('./resources/gold.png'),
                pg.image.load('./resources/pit.png'),
                pg.image.load('./resources/stench.png'),
                pg.image.load('./resources/breeze.png'),
                pg.image.load('./resources/player.png')
            ]

    return sprites




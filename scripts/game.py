import pygame as pg
import random as rnd
from enum import Enum

class Field:
    def __init__(self, pos, field_sprite, sprites, player):
        self.pos = pos
        self.sprite = field_sprite
        self.sprites = sprites
        if rnd.randint(0, 5) == 0 and pos != (0, 600):          # there is a 20% chance that a field is a pit
            self.pit = True
        else:
            self.pit = False
        if pos == [0, 600]:                   # we know that field [0, 0] is the player spawn
            self.player = True
        else:
            self.player = False
        self.pl = player
        self.breeze = False
        self.stench = False
        self.wumpus = False
        self.gold = False
        self.draw_sprites =[]


    def gen_drawing_sprites(self):
        pl_pos = self.pl.pos
        if pl_pos[0] * 200 == self.pos[0] and pl_pos[1] * 200 == self.pos[1]:
            self.player = True
        else:
            self.player = False
        self.draw_sprites = []
        if self.player:
            match self.pl.looking:
                case Direction.LEFT.value:
                    self.draw_sprites.append(self.sprites[Sprites.player_left.value])
                case Direction.RIGHT.value:
                    self.draw_sprites.append(self.sprites[Sprites.player_right.value])
                case Direction.UP.value:
                    self.draw_sprites.append(self.sprites[Sprites.player_up.value])
                case Direction.DOWN.value:
                    self.draw_sprites.append(self.sprites[Sprites.player_down.value])
        if self.breeze:
            self.draw_sprites.append(self.sprites[Sprites.breeze.value])
        if self.stench:
            self.draw_sprites.append(self.sprites[Sprites.stench.value])
        if self.wumpus:
            self.draw_sprites.append(self.sprites[Sprites.wumpus.value])
        if self.gold:
            self.draw_sprites.append(self.sprites[Sprites.gold.value])
        return

    def draw(self, root):
        root.blit(self.sprite, self.pos)
        pg.display.update()
        if not self.pit:
            if len(self.draw_sprites) != 0:
                amount = len(self.draw_sprites)
                if amount != 0:
                    sprite_height = 200 / amount
                else:
                    sprite_height = 0
                if amount > 1:
                    for i, sprite in enumerate(self.draw_sprites):
                        i += 1
                        pos = self.pos[1] + (sprite_height * (i - 1) - 20 * i)
                        pos = [self.pos[0], pos]
                        root.blit(sprite, pos)
                else:
                    root.blit(self.draw_sprites[0], self.pos)
        else:
            root.blit(self.sprites[Sprites.pit.value], self.pos)
        return root


class Player:
    def __init__(self, fields):
        self.pos = [0, 3]
        self.arrow = True
        self.looking = 1
        self.fields = fields
        return

    def turn_right(self):
        if self.looking + 1 > 3:
            self.looking = 0
        else:
            self.looking += 1
        return True

    def turn_left(self):
        if self.looking - 1 < 0:
            self.looking = 3
        else:
            self.looking -= 1
        return True

    def pick_up(self):
        if self.fields[self.pos[0]][self.pos[1]].gold:
            print('YOU WON !!!!')
            exit()

    def shoot(self):                                        # we return True or False so an AI could be implemented
        self.arrow = False                                  # more easily
        match self.looking:
            case Direction.UP.value:
                i = self.pos[0]
                while i > 0:
                    i -= 1
                    if self.fields[self.pos[0]][i].wumpus:
                        self.fields[self.pos[0]][i].wumpus = False
                        print('WUMPUS DEATH-SCREAM')
                        return True
                return False

            case Direction.DOWN.value:
                i = 3 - self.pos[0]
                while i < 3:
                    i += 1
                    if self.fields[self.pos[0]][i].wumpus:
                        self.fields[self.pos[0]][i].wumpus = False
                        print('WUMPUS DEATH-SCREAM')
                        return True
                return False

            case Direction.RIGHT.value:
                i = 3 - self.pos[1]
                while i < 3:
                    i += 1
                    if self.fields[i][self.pos[1]].wumpus:
                        self.fields[i][self.pos[1]].wumpus = False
                        print('WUMPUS DEATH-SCREAM')
                        return True
                return False

            case Direction.LEFT.value:
                i = self.pos[1]
                while i > 0:
                    i -= 1
                    if self.fields[i][self.pos[1]].wumpus:
                        self.fields[i][self.pos[1]].wumpus = False
                        print('WUMPUS DEATH-SCREAM')
                        return True
                return False

    def move(self):                         # we move in the direction we are looking in and watch out that we don't
                                            # go outside the walls aka the 4x4 play-field
        match self.looking:
            case Direction.UP.value:
                if self.pos[1] != 0:
                    self.pos[1] -= 1
                else: return False

            case Direction.RIGHT.value:
                if self.pos[0] != 3:
                    self.pos[0] += 1
                else: return False

            case Direction.DOWN.value:
                if self.pos[1] != 3:
                    self.pos[1] += 1
                else: return False

            case Direction.LEFT.value:
                if self.pos[0] != 0:
                    self.pos[0] -= 1
                else: return False


        return True



class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class Sprites(Enum):
    empty = 0
    wumpus = 1
    gold = 2
    pit = 3
    stench = 4
    breeze = 5
    player_right = 6
    player_left = 7
    player_up = 8
    player_down = 9


def load_sprites():
    sprites = [
                pg.image.load('./resources/empty_field.png'),   # 0
                pg.image.load('./resources/wumpus.png'),        # 1
                pg.image.load('./resources/gold.png'),          # 2
                pg.image.load('./resources/pit.png'),           # 3
                pg.image.load('./resources/stench.png'),        # 4
                pg.image.load('./resources/breeze.png'),        # 5
                pg.image.load('./resources/player.png'),        # 6
                pg.image.load('./resources/player_left.png'),   # 7
                pg.image.load('./resources/player_up.png'),     # 8
                pg.image.load('./resources/player_down.png')    # 9
            ]

    return sprites




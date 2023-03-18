import pygame as pg
from scripts import game

screen_size = (800, 800)
pg.init()
pg.display.set_caption('WumpusWelt')
root = pg.display.set_mode(screen_size)
sprites = game.load_sprites()
fields = []

def layout_init():
    global sprites, fields
    for x in range(0, 3):
        row =[]
        for y in range(0, 3):
            pos = [
                x * 200,
                y * 200
            ]
            row.append(game.Field(pos, sprites[game.Sprites.empty.value]))
        fields.append(row)


def main():
    running = True

    while running:


        for event in pg.event.get():
            match event.type:


                case pg.QUIT:                       # closing the program
                    running = False

if __name__ == '__main__':
    main()

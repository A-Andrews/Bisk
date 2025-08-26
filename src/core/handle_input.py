import pygame as pg

from settings import HEIGHT, WIDTH


def toggle_fullscreen(game):
    game.is_fullscreen = not game.is_fullscreen
    if game.is_fullscreen:
        display_w, display_h = pg.display.get_desktop_sizes()[0]
        game.screen = pg.display.set_mode(
            (display_w, display_h), pg.NOFRAME | pg.SCALED
        )
    else:
        pg.display.set_mode((game.width, game.height))
        game.screen = pg.display.get_surface()

    fs_flag = pg.FULLSCREEN if game.is_fullscreen else 0
    game.screen = pg.display.set_mode((WIDTH, HEIGHT), game.flags | fs_flag)


def handle_input(game):
    for e in pg.event.get():
        if e.type == pg.QUIT:
            game.running = False
        elif e.type == pg.KEYDOWN and e.key == pg.K_F12:
            toggle_fullscreen(game)
        else:
            game.scene.handle_event(e)

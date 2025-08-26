import pygame as pg

from settings import (
    ACCENT,
    BG,
    BODY_FONT_SIZE,
    BTN_HEIGHT,
    BTN_WIDTH,
    BUTTON_FONT_SIZE,
    FG,
    HEIGHT,
    START_MENU_BUTTON_SPACING,
    START_MENU_BUTTON_TOP_OFFSET,
    START_MENU_TAG_OFFSET,
    TEXT,
    TITLE_FONT_SIZE,
    WIDTH,
)
from src.core.scene import Scene
from src.ui.button import Button
from src.ui.game_screen import GameScene


class StartMenu(Scene):

    def enter(self):
        self.title_font = pg.font.Font(None, TITLE_FONT_SIZE)
        self.body_font = pg.font.Font(None, BODY_FONT_SIZE)
        self.button_font = pg.font.Font(None, BUTTON_FONT_SIZE)

        btn_w, btn_h = BTN_WIDTH, BTN_HEIGHT
        cx, cy = WIDTH // 2, HEIGHT // 2
        top = HEIGHT // 2 - START_MENU_BUTTON_TOP_OFFSET
        self.buttons = [
            Button(
                (cx - btn_w // 2, top, btn_w, btn_h),
                "Start Game",
                self.button_font,
                lambda: self.game.set_scene(GameScene),
            ),
            Button(
                (
                    cx - btn_w // 2,
                    top + btn_h + START_MENU_BUTTON_SPACING,
                    btn_w,
                    btn_h,
                ),
                "Quit",
                self.button_font,
                lambda: self.quit_game(),
            ),
        ]
        self.focus_index = 0
        self.buttons[0].focused = True

    def quit_game(self):
        self.game.running = False

    def handle_event(self, e):
        if e.type == pg.KEYDOWN:
            if e.key in (pg.K_UP, pg.K_w):
                self.move_focus(-1)
            elif e.key in (pg.K_DOWN, pg.K_s):
                self.move_focus(1)
            elif e.key in (pg.K_RETURN, pg.K_KP_ENTER):
                self.buttons[self.focus_index].on_click()
            elif e.key == pg.K_ESCAPE:
                self.quit_game()
        for b in self.buttons:
            b.handle_event(e)

    def move_focus(self, delta):
        self.buttons[self.focus_index].focused = False
        self.focus_index = (self.focus_index + delta) % len(self.buttons)
        self.buttons[self.focus_index].focused = True

    def update(self, dt):
        mouse_pos = pg.mouse.get_pos()
        for i, b in enumerate(self.buttons):
            b.update(mouse_pos)
            if b.hovered and i != self.focus_index:
                self.buttons[self.focus_index].focused = False
                self.focus_index = i
                b.focused = True

    def draw(self, surf):
        surf.fill(BG)
        title = self.title_font.render("Bisk", True, ACCENT)
        tag = self.body_font.render("Risk it for the biscuit", True, FG)
        surf.blit(
            title, title.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        )  # centre title and place it 1/3 down the screen
        surf.blit(
            tag, tag.get_rect(center=(WIDTH // 2, HEIGHT // 3 + START_MENU_TAG_OFFSET))
        )
        for b in self.buttons:
            b.draw(surf)

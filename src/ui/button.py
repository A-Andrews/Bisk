from settings import BTN, BTN_HOVER, TEXT, ACCENT
import pygame as pg

class Button:
    def __init__(self, rect, text, font, on_click, radius=14):
        self.rect = pg.Rect(rect)
        self.text = text
        self.font = font
        self.on_click = on_click
        self.radius = radius
        self.hovered = False
        self.focused = False
        self.label = self.font.render(self.text, True, TEXT)

    def update(self, mouse_pos):
        self.hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, e):
        if e.type == pg.MOUSEBUTTONDOWN and e.button == 1 and self.hovered:
            self.on_click()

    def draw(self, surf):
        color = BTN_HOVER if self.hovered else BTN
        pg.draw.rect(surf, color, self.rect, border_radius=self.radius)
        if self.focused:
            pg.draw.rect(surf, ACCENT, self.rect, width=2, border_radius=self.radius)
        surf.blit(self.label, self.label.get_rect(center=self.rect.center))

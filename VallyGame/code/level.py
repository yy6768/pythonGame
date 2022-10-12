import pygame
from settings import *
from player import *


# Level 关卡类
class Level:
    def __init__(self):
        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # 精灵的组
        self.all_sprites = pygame.sprite.Group()

        # 初始化
        self.setup()

    def setup(self):
        self.player = Player((640, 360), group=self.all_sprites)

    # dt 是 deltatime
    def run(self, dt):
        self.display_surface.fill('black')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)

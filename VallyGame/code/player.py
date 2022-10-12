import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    """
    玩家类
    pos表示玩家中心的坐标
    group是玩家所属的组
    """

    def __init__(self, pos, group):
        super().__init__(group)
        # 一般的设置
        # 玩家的图片，需要一个可绘制的surface
        self.image = pygame.Surface((32, 64))
        self.image.fill('green')
        self.rect = self.image.get_rect(center=pos)
        # 玩家移动相关的设置
        # vector2(x,y) x = 0, 左， x =1 右 y = 0 左，
        self.direction = pygame.math.Vector2()
        # rect存储的是整型值，dt需要的是float类型的值，所以不好使用
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

    def import_assets(self):
        #包含动画信息
        self.animations = {'up':[]}

    def input(self):
        keys = pygame.key.get_pressed()  # 键盘按下的键
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def move(self, dt):
        # 将方向向量normalization
        if self.direction.magnitude():
            self.direction = self.direction.normalize()
        print(self.direction)

        # horizontal movement 水平移动（TODO）
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x

        # vertical movement 垂直移动（TODO)
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

    def update(self, dt):
        self.input()
        self.move(dt)

import pygame
from settings import *
from support import *


class Player(pygame.sprite.Sprite):
    """
    玩家类
    pos表示玩家中心的坐标
    group是玩家所属的组
    """

    def __init__(self, pos, group):
        super().__init__(group)
        # 加载所有动画
        self.import_assets()
        # 格式：方向+状态（状态可以为空） exp：down（没状态的） down_axe(方向向下，状态为axe锄头
        self.status = 'down_idle'
        self.frame_index = 0
        # 一般的设置
        # 玩家的图片，需要一个可绘制的surface
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=pos)
        # 玩家移动相关的设置
        # vector2(x,y) x = 0, 左， x =1 右 y = 0 左，
        self.direction = pygame.math.Vector2()
        # rect存储的是整型值，dt需要的是float类型的值，所以不好使用
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

    def import_assets(self):
        # 包含动画信息
        self.animations = {'up': [], 'down': [], 'left': [], 'right': [],
                           'up_idle': [], 'down_idle': [], 'left_idle': [], 'right_idle': [],
                           'up_hoe': [], 'down_hoe': [], 'left_hoe': [], 'right_hoe': [],
                           'up_axe': [], 'down_axe': [], 'left_axe': [], 'right_axe': [],
                           'up_water': [], 'down_water': [], 'left_water': [], 'right_water': []}
        for animation in self.animations.keys():
            full_path = '../graphics/character/' + animation
            self.animations[animation] = import_folder(full_path)
        print(self.animations)

    # 当前动画
    def animate(self, dt):
        self.frame_index += 4 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0

        self.image = self.animations[self.status][int(self.frame_index)]

    # 玩家的输入
    def input(self):
        keys = pygame.key.get_pressed()  # 键盘按下的键
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = 'up'
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = 'left'
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = 'right'
        else:
            self.direction.x = 0

    def get_status(self):
        # 如果玩家没有移动
        # add idle 到状态结尾
        if self.direction.magnitude() == 0:
            self.status = self.status.split('_')[0] + '_idle'

    def move(self, dt):
        # 将方向向量normalization
        if self.direction.magnitude() > 0:
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
        self.get_status()
        self.move(dt)
        self.animate(dt)

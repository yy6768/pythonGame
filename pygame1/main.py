import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((400, 400))

pygame.display.set_caption("hello world")

f = pygame.font.Font('C:/Windows/Fonts/simhei.ttf', 50)

text = f.render("hello world", True, (0, 0, 255), (255, 255, 255))

# 获得显示对象的区域坐标
textRect = text.get_rect()

textRect.center = (200, 200)

screen.blit(text, textRect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.flip()  # 更新

"""
Title: 
Date: 2023-05-16 20:18:35
LastEditTime: 2023-05-17 16:38:30
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""

import sys

import pygame
from ship import Ship

from settings import Settings


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 监视键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # 每次循环时都重绘屏幕
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # 让最近绘制的屏幕可见
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()

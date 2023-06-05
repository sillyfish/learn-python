"""
Title: 
Date: 2023-05-17 16:53:46
LastEditTime: 2023-05-17 16:53:46
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""


class Settings:
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的静态设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_speed = 1.5
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # 外星人设置
        self.fleet_drop_speed = 10

        # 游戏节奏加快速度
        self.speedup_scale = 1.1
        # 外星人点数提高速度
        self.scores_scale = 1.5

        self.high_score_file = "high_score.txt"

    def initialize_dynamic_settings(self, speed_up):
        """初始化随游戏进行而变化的设置"""
        speed_up += 1
        self.ship_speed = 1.5 * speed_up
        self.bullet_speed = 2.5 * speed_up
        self.alien_speed = 1.0 * speed_up

        # fleet_direction为1表示向右; 为-1表示向左
        self.fleet_direction = 1

        # 记分
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.scores_scale)

import sys
import pygame  #导入了sys和pygame模块
import game_functions as gf

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import  Ship
from pygame.sprite import Group
from alien import Alien


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init() #初始化背景设置
    ai_settings = Settings()
    # 调用pygame中的display.set_mode函数来创建显示窗口
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #创建play按钮
    play_button = Button(ai_settings,screen,"Play")
    #创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)


    #创建一艘飞船
    ship = Ship(ai_settings,screen)
    #创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个外星人
    aliens = Group()

    #创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)


    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
            gf.update_screen(ai_settings,screen,ship,aliens,bullets)
        gf.update_aliens(ai_settings,screen,stats,ship,aliens,bullets,play_button)


run_game()
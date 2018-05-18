import pygame.font
from pygameProj.game import ship
from pygame.sprite import Group



class Scoreboard():

    def __init__(self, ai_settings, screen, stats):
        '''厨师胡显示得分的属性'''
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.high_score = 0
        #显示得分信息时使用的字体
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.ships = Group()
        #准备初始化得分图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        '''将得分转换成渲染的图像'''
        round_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(round_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # 将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20


    def prep_high_score(self):
        '''将得分转换成渲染的图像'''
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)

        # 将得分放在屏幕顶部中央s
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 20


    def prep_level(self):
        '''将等级渲染成图像'''
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)
        #将等级放在得分下面
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        '''显示还剩下多少艘飞船'''
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ai_ship = ship.Ship(self.ai_settings, self.screen)
            ai_ship.rect.x = 10 + ship_number * ai_ship.rect.width
            ai_ship.rect.y = 10
            self.ships.add(ai_ship)

    def show_score(self):
        '''在屏幕上显示得分'''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        #绘制飞船
        self.ships.draw(self.screen)


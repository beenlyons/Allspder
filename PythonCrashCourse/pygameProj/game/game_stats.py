class GameStats():
    '''跟踪游戏信息'''

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        #不应该重置最高分
        self.high_score = 0
        self.level = 1

    def reset_stats(self):
        '''初始化游戏运行期间可能变化的统计信息'''
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0




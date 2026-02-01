class Settings:
    """储存游戏《外星人入侵》中所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0,0,0)

        #飞船设置
        self.ship_limit = 2
        
        #子弹设置
        self.bullet_width = 4
        self.bullet_height = 6
        self.bullet_color = (255,215,0)
        self.bullets_allowed = 12
        
        #外星人设置
        self.fleet_drop_speed = 10
        
        #以什么速度加快游戏的节奏
        self.speedup_scale = 1.3
        #外星人份数的提高速度
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed = 5
        self.bullet_speed = 3
        self.alien_speed = 1.0
        
        #fleet_direction为1表示向右，为-1表示向左
        self.fleet_direction = 1
        
        #计分设置
        self.alien_points = 50
    
    def increase_speed(self):
        """提高速度设置的值"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard:
    """"显示得分信息的类"""
    
    def __init__(self, ai_game):
        """"初始化显示得分涉及的属性"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        
        #显示得分信息时使用的字体设置
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)
        
        #等级的字体大小设置
        self.level_font = pygame.font.SysFont(None, 36)
        
        #准备最高分和当前得分的图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
    
    def prep_score(self):
        """将得分渲染为图像"""
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(score_str,True,
            self.text_color,self.settings.bg_color)
        
        #在屏幕右上角显示得分
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def prep_high_score(self):
        """"将最高分渲染为图像"""
        high_score = round(self.stats.high_score,-1)
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True,
            self.text_color, self.settings.bg_color)
        
        #将最高分放在屏幕顶部的中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
        
    def show_score(self):
        """在屏幕上显示当前得分、最高分、等级和余下的飞船数"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
        
    def check_high_score(self):
        """检查是否诞生了新的最高分"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
    
    def prep_level(self):
        """将等级渲染为图像"""
        level_str = f"Lv{self.stats.level}"
        level_color = (255, 215, 0)
        self.level_image = self.level_font.render(level_str, True,
            level_color, self.settings.bg_color)
        
        #将等级放在左上角
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.screen_rect.left + 15
        self.level_rect.top = self.screen_rect.top + 20

    def prep_ships(self):
        """在等级右边，显示还剩几条命（几艘飞船）"""
        self.ships = Group()

        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            
            # 缩小飞船图像到原来的1/2
            original_img = ship.image
            new_size = (original_img.get_width() // 2, 
                        original_img.get_height() // 2)
            
            ship.image = pygame.transform.smoothscale(original_img, new_size)
            ship.rect = ship.image.get_rect()  # 更新 rect
            
            # 位置，y垂直居中对齐Lv1文字再向上微调2
            ship.rect.x = self.level_rect.right + 15 + \
                        ship_number * (new_size[0] + 8)
            ship.rect.y = self.level_rect.centery - new_size[1] // 2 - 2
            
            self.ships.add(ship)
import pygame.font

class Button:
    """为游戏创建按钮的类"""
    
    def __init__(self, ai_game, msg):
        """初始化按钮的属性"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        
        # 设置按钮的尺寸和其他属性
        self.width, self.height = 100, 40
        self.button_color = (220, 180, 60)
        self.text_color = (0,0,0)
        self.font = pygame.font.SysFont("Impact", 32)
        
        # 创建按钮的rect对象，并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        # 按钮的标签只需创建一次
        self._prep_msg(msg)
    
    def _prep_msg(self, msg):
        """将msg渲染为图像,并使其在按钮上居中"""
        self.msg_image = self.font.render(msg, False, self.text_color,
            self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        """绘制圆角按钮 + 连续的外部描边"""
        # 先画稍大的圆角矩形作为描边
        pygame.draw.rect(
            self.screen,
            (245,222,111),            # 描边颜色
            self.rect.inflate(6, 6),  # 比按钮大6像素（左右各3，上下共6）
            border_radius=23          # 比按钮的圆角再大一点
        )

        # 再画主按钮（盖住中间部分）
        pygame.draw.rect(
            self.screen,
            self.button_color,
            self.rect,
            border_radius=21
        )

        # 文字
        self.screen.blit(self.msg_image, self.msg_image_rect)
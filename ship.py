import pygame

class Ship():
    """创建一个飞船，并对其进行管理"""
    
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings
        
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # 将每艘飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的center属性中存储最小值
        self.centerx = float(self.rect.centerx)

        # 初始化键盘输入
        self.moving_right = False
        self.moving_left = False

        
    def update(self):
        """根据键盘输入调整center值从而更新飞船位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.centerx -= self.ai_settings.ship_speed_factor

        # 根据self.centerx更新rect对象
        self.rect.centerx = self.centerx
        
        
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)


    def center_ship(self):
        """让飞船在屏幕底部居中"""
        self.center = self.screen_rect.centerx
    

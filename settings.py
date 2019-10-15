class Settings():
    """存储《外星人入侵》的所有类"""
    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width=1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_hight = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 20
        
        # 外星人设置
        self.alien_speed_factor = 1
        self.aliens_drop_speed = 5
        # 1表示向右移动，-1表示向左移动
        self.aliens_speed_direction = 1
        




class setting:
    def __init__(self) -> None:
        self.screen_width=1000
        self.screen_height=600
        self.color=(200,200,255)
        
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(0,0,0)
        #游戏节奏变化步长
        self.change_scale=2
        
        self.init_dynamic_setting()
    
    def init_dynamic_setting(self):
        self.ship_number=3
        self.ship_speed=0.5
        self.bullet_speed=1
        self.alien_number=5
        self.alien_speed=0.25

    def speed_up(self):
        self.ship_speed*=self.change_scale
        self.bullet_speed*=self.change_scale
        self.alien_number*=self.change_scale
        self.alien_speed*=self.change_scale

    

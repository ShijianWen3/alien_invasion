import pygame
from bullet import bullet

#ship类创建
class Ship:
    def __init__(self,screen:pygame.Surface) -> None:
        #画布，是显示对象的方式
        self.screen=screen
        self.image=pygame.image.load('./images/ship.bmp')
        #ship外接矩形
        self.rect=self.image.get_rect()
        #画布外接矩形
        self.screen_rect=self.screen.get_rect()
        #通过控制外接矩形的位置然后在矩形位置绘制图形控制对象移动
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom-50

        self.temp_x=(float)(self.screen_rect.centerx)
        self.state=None
        # self.move_speed=0.5

        self.ship_state=None

    def blit_ship(self):
        self.screen.blit(self.image,self.rect)

    def move(self,setting):
        if self.state is None:
            return
        
        if self.state:
            self.temp_x+=setting.ship_speed
            self.rect.centerx=(int)(self.temp_x)
            if (self.rect.centerx+(self.rect.size[0])/2)>self.screen_rect.size[0]:
                self.rect.centerx=(self.rect.size[0])/2
                self.temp_x=(float)(self.rect.centerx)
        else:
            self.temp_x-=setting.ship_speed
            self.rect.centerx=(int)(self.temp_x)
            if (self.rect.centerx-(self.rect.size[0])/2)<0:
                self.rect.centerx=self.screen_rect.size[0]-((self.rect.size[0])/2)
                self.temp_x=(float)(self.rect.centerx)

    def update_state(self,elements):
        if self.ship_state is None:
            return
        if self.ship_state=='Offense':
            new_bullet=bullet(elements.ship,elements.screen,elements.setting)
            elements.bullets.add(new_bullet)

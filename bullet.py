import pygame
from pygame.sprite import Sprite
#子弹类创建
class bullet(Sprite):
    def __init__(self,ship,screen,setting) -> None:
        super().__init__()
        self.screen=screen
        self.color=setting.bullet_color
        # self.speed=setting.bullet_speed
        
        self.rect=pygame.Rect(0,0,setting.bullet_width,setting.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top
        self.tmp_y=(float)(self.rect.centery)

    def move(self,setting):
        self.tmp_y-=setting.bullet_speed
        self.rect.centery=(int)(self.tmp_y)
        

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)

def killed_aliens(elements):
    #检测rect是否碰撞,返回发生碰撞对象构成的字典，True代表碰撞之后删除对应元素
    collision=pygame.sprite.groupcollide(elements.bullets,elements.aliens,True,True)
    if collision:
        elements.user.score_add(5)



        

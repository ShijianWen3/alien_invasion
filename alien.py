"""外星人"""
import pygame
from pygame.sprite import Sprite
import random as ra
class Alien(Sprite):
    def __init__(self,screen:pygame.Surface) -> None:
        super().__init__()
        self.screen=screen
        self.image=pygame.image.load('./images/alien.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()
        self.rect.centerx=50+100*ra.randint(0,9)
        self.tmp_x=(float)(self.rect.centerx)
        self.rect.top=self.screen_rect.top+100*ra.randint(0,1)
        self.dir=ra.choice([-1,1])


    def blit_alien(self):
        self.screen.blit(self.image,self.rect)

    def move(self,setting):
        if self.rect.centerx<50:
            self.tmp_x=(float)(950)
            self.rect.centery+=setting.alien_speed*100
            
        elif self.rect.centerx>950:
            self.tmp_x=(float)(50)
            self.rect.centery+=setting.alien_speed*100
            
        self.tmp_x+=self.dir*setting.alien_speed
        self.rect.centerx=(float)(self.tmp_x)

    
        
        
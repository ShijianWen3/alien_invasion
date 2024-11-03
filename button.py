import pygame
from ship import Ship
class Button:
    def __init__(self,screen:pygame.surface,msg) -> None:
        #初始化按钮属性
        self.screen=screen
        self.screen_rect=self.screen.get_rect()
        #初始化按钮尺寸及其他
        self.width,self.height=200,50
        self.button_color=(0,135,0)
        self.text_color=(255,255,255)
        self.font=pygame.font.SysFont(None,48)
        #创建按钮的rect对象
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center

        #按钮的标签(创建一次)
        self._prep_msg(msg)

    def _prep_msg(self,msg):
        #将msg字符串渲染成图像
        self.msg_image=self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center
    
    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)

    def check_mouse(self,elements):
        if self.rect.collidepoint(elements.mouse_position):
            elements.states.reset_states()
            elements.states.gamestate=True

            #清空外星人和子弹列表
            elements.aliens.empty()
            elements.bullets.empty()
            #相关设置复位
            elements.setting.init_dynamic_setting()
            #user得分和等级复位
            elements.user.reset()
            #飞船复位
            elements.ship=Ship(elements.screen)
            #光标不可见
            pygame.mouse.set_visible(False)





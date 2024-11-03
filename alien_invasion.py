import pygame,sys
import game_function as gf
from Setting import setting
from game_state import GameState
from ship import Ship
from alien import Alien
from pygame.sprite import Group
from button import Button
from user import User
from text_display import TextDisplay
class game_elements:
    def __init__(self) -> None:
        #创建设置实例
        self.setting=setting()
        #创建状态类实例
        self.states=GameState(self.setting)
        #显示窗口画布
        self.screen=pygame.display.set_mode((self.setting.screen_width,self.setting.screen_height))
        pygame.display.set_caption('Alien Invasion')
        # self.screen.fill(self.setting.color)
        #创建user实例
        self.user=User()
        #创建ship实例
        self.ship=Ship(self.screen)
        #创建子弹实例编组
        self.bullets=Group()
        #创建alien外星人实例编组
        self.aliens=Group()
        #创建按钮
        self.play_button=Button(self.screen,'Play')
        #记录鼠标点击坐标
        self.mouse_position=None
        #创建积分板
        self.score_board=TextDisplay(self)
        #创建最高分板
        self.MaxScore_board=TextDisplay(self)
        #创建等级板
        self.level_board=TextDisplay(self)
        #创建信息板
        self.info_board=TextDisplay(self)
        



def run_game():
    
    #__init__
    pygame.init()
    elements=game_elements()
    while True:
        #检测事件
        gf.check_event(elements)  
        elements.screen.fill(elements.setting.color)  
        if elements.states.gamestate:
            #加载alien类
            gf.update_aliens(elements)
            gf.check_alien(elements)
            #加载子弹bullet类
            gf.update_bullets(elements)
            #加载ship类
            gf.update_ship(elements)
            #加载显示文本
            gf.content_display(elements)
            #清除无用元素
            gf.remove_trash(elements)
            #检查玩家状态
            gf.check_user(elements)
        else:
            elements.play_button.draw_button()
        #更新屏幕
        # gf.update_screen(elements)
        pygame.display.flip()
if __name__=='__main__':
    run_game()

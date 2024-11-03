import pygame,sys,time

from bullet import bullet,killed_aliens
from alien import Alien
from pygame.sprite import Group
from ship import Ship
def check_event(elements):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        
        if event.type==pygame.KEYDOWN:
            keydown_event(elements,event)
        elif event.type==pygame.KEYUP:
            keyup_event(elements,event)
        elif event.type==pygame.MOUSEBUTTONDOWN:
            elements.mouse_position=pygame.mouse.get_pos()
            if not elements.states.gamestate:
                elements.play_button.check_mouse(elements)

def keydown_event(elements,event=None):
    #后续希望改为match实现
    if event.key==pygame.K_q:
        elements.user.storage_max()
        sys.exit()
    if event.key==pygame.K_p:
        elements.user.storage_max()
        elements.states.gamestate=False
        #光标可见
        pygame.mouse.set_visible(True)
    if event.key==pygame.K_SPACE:
        new_bullet=bullet(elements.ship,elements.screen,elements.setting)
        elements.bullets.add(new_bullet)
        
    if (event.key==pygame.K_RIGHT) or (event.key==pygame.K_d):
        elements.ship.state=True
    elif (event.key==pygame.K_LEFT) or (event.key==pygame.K_a):
        elements.ship.state=False

def keyup_event(elements,event=None):
    if event.key in [pygame.K_RIGHT,pygame.K_d,pygame.K_LEFT,pygame.K_a]:
        elements.ship.state=None
    if event.key==pygame.K_SPACE:
        elements.bullets.state=False

def update_aliens(elements):
    #aliens精灵组小于设定值时自动补充
    if elements.aliens.__len__()<elements.setting.alien_number:
        new_alien=Alien(elements.screen)
        elements.aliens.add(new_alien)
    for alien in elements.aliens:
        alien.move(elements.setting)
        alien.blit_alien()

def update_bullets(elements):
    for bullet in elements.bullets:
        #更新bullet位置
        bullet.move(elements.setting)
        #绘制bullet
        bullet.draw_bullet()
    killed_aliens(elements)

def update_ship(elements):
    #更新ship位置
    elements.ship.move(elements.setting)
    #绘制ship
    elements.ship.blit_ship()
    #加载ship状态
    elements.ship.update_state(elements)


def check_alien(elements):
    #alien越过防线
    for alien in elements.aliens:
        if alien.rect.centery>=elements.ship.rect.centery:
            if elements.states.ship_left<=1:
                elements.states.gamestate=False
            else:
                elements.states.ship_left-=1
            time.sleep(0.5)
            #清空alien精灵组
            elements.aliens.empty()
            elements.ship=Ship(elements.screen)
    #检测ship是否和alien相撞
    #函数用来检测一个sprite和一个编组中的sprite是否有相撞
    if pygame.sprite.spritecollideany(elements.ship,elements.aliens):
        if elements.states.ship_left<=1:
                elements.states.gamestate=False
        else:
            elements.states.ship_left-=1
        time.sleep(0.5)
         #清空alien精灵组
        elements.aliens.empty()
        elements.ship=Ship(elements.screen)
#屏幕上文字内容显示
def content_display(elements):
    elements.score_board.display('Score:'+str(elements.user.score),elements.setting.screen_width-120,20)
    elements.score_board.display('Level:'+str(elements.user.level),
                                 elements.setting.screen_width-120,
                                 elements.setting.screen_height-20)

    elements.info_board.display('Restart:P,Exti:Q',100,elements.setting.screen_height-20,20)
    elements.MaxScore_board.display('Max:'+str(elements.user.MaxScore),elements.setting.screen_width/2,20)
#检测玩家等级是否应该提升
def check_user(elements):
    level=elements.user.level
    last_level=elements.user.last_level
    if level%3==0 and level>last_level:
        elements.setting.speed_up()
        elements.user.last_level=level
#移除每用的子弹类
def remove_trash(elements):
    for bullet in elements.bullets.copy():
        if bullet.rect.bottom <= 0:
            elements.bullets.remove(bullet)
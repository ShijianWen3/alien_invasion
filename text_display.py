import pygame

class TextDisplay:
    def __init__(self,elements) -> None:
         self.screen=elements.screen
         self.screen_rect=self.screen.get_rect()
         self.setting=elements.setting

         self.text_color=(30,30,30)
         self.font=pygame.font.SysFont(None,48)

         

    def display(self,text:str,pos_x:int,pos_y:int,size:int=None):
         if size is not None:
              self.font=pygame.font.SysFont(None,size)

         self.display_image=self.font.render(text,True,self.text_color,self.setting.color)
         self.display_rect=self.display_image.get_rect()
         self.display_rect.centerx=pos_x
         self.display_rect.centery=pos_y
         self.screen.blit(self.display_image,self.display_rect)




         


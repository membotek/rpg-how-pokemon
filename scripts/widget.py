import pygame
from scripts import util
class Button:
    def __init__(self,x,y,hight,width,text,color=(0,0,0),hovercolor=(255,255,255)):
        self.x=x
        self.y=y
        self.color=color
        self.hovercolor=hovercolor
        self.size=hight,width
        self.slot=None
        self.rect=pygame.Rect(self.x,self.y,*self.size)
        self.hoverd=False
        font=pygame.font.Font('graphics/font/SourceCodePro-SemiboldIt.otf',45)
        self.image=font.render(text,True,(0,0,0))
        self.image=pygame.transform.scale(self.image,(self.size))
        print(self.size,self.x,self.y)
    def update(self):
        xy=pygame.mouse.get_pos()
        xy=list(xy)
        xy[0]//=2
        xy[1]//=2
        if self.rect.collidepoint(xy):
            self.hoverd=True
            if pygame.mouse.get_pressed()[0]:
                if self.slot!=None:
                    self.slot()
        else:
            self.hoverd=False
    def render(self,display):
        if self.hoverd==False:
            display.blit(self.image,(self.x,self.y))
        else:
            pygame.draw.rect(display,self.hovercolor,(self.x,self.y,*self.size),100)
            display.blit(self.image,(self.x,self.y))

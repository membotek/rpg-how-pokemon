import pygame
from scripts import util
class Button:
    def __init__(self,x,y,hight,width,pathforimage,color=(0,0,0),hovercolor=(255,255,255)):
        self.x=x
        self.y=y
        self.color=color
        self.hovercolor=hovercolor
        self.size=hight,width
        self.slot=None
        self.rect=pygame.Rect(self.x,self.y,*self.size)
        self.hoverd=False
        self.image=util.loadimage(pathforimage,1)
        self.image=pygame.transform.scale(self.image,(self.size))
    def update(self):
        xy=pygame.mouse.get_pos()
        if self.rect.collidepoint(xy):
            self.hoverd=True
            if pygame.mouse.get_pressed()[0]:
                if self.slot!=None:
                    self.slot()
        else:
            self.hoverd=False
    def render(self,display):
        if self.hoverd==False:
            pygame.draw.rect(display,self.color,(self.x-10,self.y-10,self.size[0]+10,self.size[1]+10),10)
            display.blit(self.image,(self.x,self.y))
        else:
            pygame.draw.rect(display,self.hovercolor,(self.x,self.y,*self.size),100)
            display.blit(self.image,(self.x,self.y))
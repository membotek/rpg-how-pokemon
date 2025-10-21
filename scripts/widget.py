import pygame
import random
from scripts import util,batlmeny

class Button:
    def __init__(self,menu,x,y,hight,width,text,color=(0,0,0),hovercolor=(255,255,255)):
        self.menu=menu
        self.text=text
        self.x=x
        self.y=y
        self.color=color
        self.hovercolor=hovercolor
        self.size=hight,width
        self.slot=None
        self.slot2=None
        self.inermenu=None
        self.rect=pygame.Rect(self.x,self.y,*self.size)
        self.hoverd=False
        font=pygame.font.Font('graphics/font/SourceCodePro-SemiboldIt.otf',45)
        self.image=font.render(text,True,(0,0,0))
        self.image=pygame.transform.scale(self.image,(self.size))
        self.orgtext=text
        self.countclicks=0

    def update(self):
        xy=pygame.mouse.get_pos()
        xy=list(xy)
        xy[0]//=2
        xy[1]//=2
        if self.rect.collidepoint(xy):
            self.hoverd=True
            if self.menu.click==True:
                self.countclicks+=1
                self.menu.active=self
                if self.slot!=None and self.countclicks==1:
                    self.slot()
                if self.slot2!=None and self.countclicks==2:
                    self.slot2()
                if self.countclicks>=2:
                    self.countclicks=0
                
                if self.text=='run away':
                    a=random.randint(1,50)
                    a*=(self.menu.player.level//4)
                    if batlmeny.active==0:
                        if 25<a:
                            self.menu.retturn=True
                            self.menu.inftext=None
                            self.menu.active=0
                            batlmeny.active=0
                        else:
                            batlmeny.active=1


        
        else:
            self.hoverd=False
            if self.menu.click==True:
                self.countclicks=0
                self.changetext(self.orgtext)
        if self.menu.active==self and self.inermenu!=None:
            self.inermenu.update()

    def render(self,display):
        if self.menu.active==self:
            pygame.draw.rect(display,self.hovercolor,(self.x,self.y,*self.size),100)
            display.blit(self.image,(self.x,self.y))
        elif self.hoverd==False:
            display.blit(self.image,(self.x,self.y))
        else:
            pygame.draw.rect(display,self.hovercolor,(self.x,self.y,*self.size),100)
            display.blit(self.image,(self.x,self.y))
        if self.menu.active==self and self.inermenu!=None:
            self.inermenu.render(display)
    def changetext(self,newtext):
        font=pygame.font.Font('graphics/font/SourceCodePro-SemiboldIt.otf',45)
        self.image=font.render(str(newtext),True,(0,0,0))
        self.image=pygame.transform.scale(self.image,(self.size))

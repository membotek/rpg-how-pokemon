import pygame
from scripts import util,map
class Object:
    def __init__(self,x,y,path,scale):
        self.x=x
        self.y=y
        self.image=util.loadimage(path,scale)
    def render(self,display,camera):
        display.blit(self.image,(self.x-camera[0],self.y-camera[1]))
    def update(self):
        pass
    def get_boundbox(self,display):
        bbobj=pygame.Rect(self.x,self.y,self.image.get_width(),self.image.get_height())
        return(bbobj)
import pygame
from scripts import util,map,player
class Object:
    def __init__(self,x,y,path,scale,):
        self.x=x
        self.y=y
        self.image=util.loadimage(path,scale)
    def render(self,display,camera,mainplayer):
        bbdetect=pygame.Rect(mainplayer.x-64,mainplayer.y-64,64*3,64*3)
        if bbdetect.colliderect(self.get_boundbox()):
            pass
            # display.blit(self.image,(self.x-camera[0],self.y-camera[1]))

    def update(self):
        pass
    def get_boundbox(self):
        bbobj=pygame.Rect(self.x,self.y,self.image.get_width(),self.image.get_height())
        return(bbobj)
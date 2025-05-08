import pygame
from scripts import util
class Map:
    def __init__(self):
        self.path=util.loadimage('C:/Users/Makar/new_after_test_game/maps/map.png')
        self.camera=[0,0]
        self.border=util.loadbordermapfromcsv('C:/Users/Makar/new_after_test_game/maps/border_Tile Layer 1_border.csv')
    def render(self,display):
        display.blit(self.path,(0-self.camera[0],0-self.camera[1]))
        for i in self.border:
            bb=pygame.Rect(i[1]*64,i[0]*64,64,64)
            # pygame.draw.rect(display,(255,0,0),(bb.x-self.camera[0],bb.y-self.camera[1],64,64))
    def getcollidite(self,hb):
        lx=hb.left//64
        rx=hb.right//64+1
        dy=hb.bottom//64+1
        uy=hb.top//64
        tyles=[]
        for i in range(lx,rx+1):
            i*64
            for g in range(uy,dy+1):
                if (i,g) in self.border:
                    ss=pygame.Rect(i*64,g*64,64,64)
                    if ss.colliderect(hb):
                        tyles.append(ss)
        return(tyles)
    def getcollideNotEffective(self,hb):
        spisok=[]
        for i in self.border:
            bb=pygame.Rect(i[1]*64,i[0]*64,64,64)
            if bb.colliderect(hb):
                spisok.append(bb)
        return(spisok)
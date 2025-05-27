import pygame
import csv
from scripts import util,obj
class Map:
    def __init__(self):
        self.path=util.loadimage('maps/map.png')
        self.camera=[0,0]
        self.border=util.loadbordermapfromcsv('maps/border_Tile Layer 1_border.csv')
        self.objects=self.loadobjectsfromcssv('maps/border_Tile Layer 1_objects.csv',1)
        self.forest=util.loadimage('maps/forest.png',1,(0,0,0))

    def render(self,display,mainplayer):
        display.blit(self.path,(0-self.camera[0],0-self.camera[1]))
        for i in self.border:
            bb=pygame.Rect(i[1]*64,i[0]*64,64,64)
            # pygame.draw.rect(display,(255,0,0),(bb.x-self.camera[0],bb.y-self.camera[1],64,64))
    def renderforest(self,display):
        display.blit(self.forest,(0-self.camera[0],0-self.camera[1]))
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
    def loadobjectsfromcssv(self,path,scale):
        objs={}
        nomberstr=-1
        nombersto=-1
        border=set()
        f=open(path)
        file=csv.reader(f,delimiter=',')
        for i in file:
            nomberstr+=1
            nombersto=-1
            for g in i:
                nombersto+=1
                g=int(g)
                if g==3:
                    objs[(nomberstr,nombersto)]=obj.Object(nombersto*64,nomberstr*64-64,'C:/Users/Makar/rpg-how-pokemon/graphics/objects/02.png',scale)
                if g==4:
                    objs[(nomberstr,nombersto)]=obj.Object(nombersto*64,nomberstr*64-64,'C:/Users/Makar/rpg-how-pokemon/graphics/objects/03.png',scale)
        return(objs)
from scripts import util,player
import pygame
import os
import csv
import math
import random


class Detail:
    def __init__(self,x,y,id,mainplayer):
        self.x=x
        self.y=y
        self.clas=None
        self.player=mainplayer
        self.maincolor=(0,0,0)
        if 0<=id<=15:
            ids=[id,0]
            self.image=util.slise('graphics/tilemap/details.png',nomber=ids)
            self.maincolor=(200,150,125)
        if 16<=id==16:
            ids=[0,1]
            self.image=util.slise('graphics/tilemap/details.png',nomber=ids)
            self.maincolor=(102,102,153)
            self.clas='rock'
        if 32<=id<=39:
            ids=[id-32,2]
            self.image=util.slise('graphics/tilemap/details.png',nomber=ids)
            self.maincolor=(164,196,0)
            self.clas='grass'
        if 48<=id<=55:
            ids=[id-48,3]
            self.image=util.slise('graphics/tilemap/details.png',nomber=ids)
            self.maincolor=(225,255,225)
            self.clas='grass'
        if 0<=id<=3:
           self.clas= 'grass'
        if 4<=id<=4:
            self.clas='rock'
        if 5<=id<=8:
            self.clas='wood'
        if 9<=id<=12:
            self.clas='rock'
        if 13<=id<=14:
            self.clas='bone'
        if 15<=id<=15:
            self.clas='rock'
    
    def render(self,display,camera):
        display.blit(self.image,(self.x-camera[0],self.y-camera[1]))

    def anigelastion(self,popkorn,detailslist):
        pop=[]
        if self.player.fight==True:
            pop=self.player.atack()
            if self.x//64==(pop[0]+pop[2])//64 and self.y//64==(pop[1]+pop[3])//64 or self.x//64==pop[0]//64 and self.y//64==pop[3]//64:
                for i in range(random.randint(24,50)):
                    popkorn.append(Partikal(self.x,self.y,self.maincolor))
                detailslist.remove(self)
            if self.player.secterboundbox.colliderect(self.get_boundbox()):
                for i in range(random.randint(24,50)):
                    popkorn.append(Partikal(self.x,self.y,self.maincolor))
                self.player.bag.saveinventory(self.clas)
                if self in detailslist:
                    detailslist.remove(self)

    def get_boundbox(self):
        bbobj=pygame.Rect(self.x,self.y,self.image.get_width(),self.image.get_height())
        return(bbobj)
    
def loaddetailsfromscv(path,mainplayer):
    nomberstr=-1
    nombersto=-1
    picturs=[]
    f=open(path)
    file=csv.reader(f,delimiter=',')
    for i in file:
        nomberstr+=1
        nombersto=-1
        for g in i:
            nombersto+=1
            if 0<=int(g)<=55:
                lol=Detail(nombersto*64,nomberstr*64,int(g),mainplayer)
                picturs.append(lol)
    return(picturs)

class Partikal:
    def __init__(self,x,y,maincolor):
        self.x=x+32
        self.y=y+32
        self.timer=random.randint(4,10)
        self.color=maincolor
        self.spead=4
        self.angle=(random.random()-0.5)*2*math.pi
        self.vx=self.spead*math.cos(self.angle)
        self.vy=self.spead*math.sin(self.angle)

    def render(self,display,camera):
        pygame.draw.circle(display,self.color,(self.x-camera[0],self.y-camera[1]),5)
        
    def update(self,popkorn):
        self.timer-=1
        self.x+=self.vx
        self.y+=self.vy
        if self.timer<=0:
            popkorn.remove(self)
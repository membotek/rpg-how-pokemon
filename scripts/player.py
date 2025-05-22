import pygame
from scripts import util,map,setings,animation,obj
class Player:
    def __init__(self,x,y,spead,map):
        self.x=x
        self.y=y
        self.moveright=False
        self.moveleft=False
        self.moveup=False
        self.movedown=False
        self.fight=False
        self.nowweapons='axe'
        self.timeratack=0
        self.spead=spead
        self.map=map
        self.nowanim='down'
        self.path=util.loadimage('C:/Users/Makar/new_after_test_game/maps/map.png')
        self.playerphoto=util.loadimage('C:/Users/Makar/new_after_test_game/graphics/player/down/down_0.png',1,(255,255,255))
        self.listweapons={
            'axe':util.loadnameimages('graphics/weapons/axe',1)
        }
        self.animations={
            'right':animation.Animation('C:/Users/Makar/rpg-how-pokemon/graphics/player/right',5),
            'left':animation.Animation('C:/Users/Makar/rpg-how-pokemon/graphics/player/left',5),
            'down':animation.Animation('C:/Users/Makar/rpg-how-pokemon/graphics/player/down',5),
            'up':animation.Animation('C:/Users/Makar/rpg-how-pokemon/graphics/player/up',5),
            'idleright':animation.Animation('graphics/player/right_idle',5),
            'idleleft':animation.Animation('graphics/player/left_idle',5),
            'idledown':animation.Animation('graphics/player/down_idle',5),
            'idleup':animation.Animation('graphics/player/up_idle',5),
            'fightright':animation.Animation('graphics/player/right_attack',5),
            'fightleft':animation.Animation('graphics/player/left_attack',5),
            'fightdown':animation.Animation('graphics/player/down_attack',5),
            'fightup':animation.Animation('graphics/player/up_attack',5),
        }
    def render(self,display,camera):
        if self.fight==True:
            pass
        self.animations[self.nowanim].render(display,self.x-camera[0],self.y-camera[1])
    def update(self,display):
        self.animations[self.nowanim].udate()
        spead=self.spead
        if (self.moveright or self.moveleft) and (self.movedown or self.moveup):
            spead/=1.41
        if self.x>=self.path.get_width()-self.playerphoto.get_width():
            self.x=self.path.get_width()-self.playerphoto.get_width()
        if self.x<=0:
            self.x=0
        if self.y>=self.path.get_height()-self.playerphoto.get_height():
            self.y=self.path.get_height()-self.playerphoto.get_height()
        if self.y<=0:
            self.y=0
        if self.moveright==False and self.moveleft==False and self.moveup==False and self.movedown==False:
            b=self.getboundbox().center
            self.x=b[0]//64*64
            self.y=b[1]//64*64
            if self.nowanim in ('right','left','up','down'):
                self.nowanim='idle'+self.nowanim
        self.movey(self.spead)
        self.movex(self.spead)
        if self.fight==True:
            if 'fight' in self.nowanim:
                pass
            elif 'idle' in self.nowanim:
                self.nowanim='fight'+self.nowanim[4:]
            else:
                self.nowanim='fight'+self.nowanim
            self.timeratack-=1
            if self.timeratack<=0:
                self.nowanim=self.nowanim[5:]
                self.fight=False

    def getboundbox(self):
        bh=pygame.Rect(self.x,self.y,64,64)
        return(bh)
    def movex(self,spead):
        n=[]
        if self.moveright:
            self.nowanim='right'
            self.x+=spead
            boom=self.map.getcollideNotEffective(self.getboundbox())
            for i in boom:
                self.x=i.left-self.playerphoto.get_width()
        if self.moveleft:
            self.nowanim='left'
            self.x-=spead
            boom=self.map.getcollideNotEffective(self.getboundbox())
            for i in boom:
                self.x=i.right
    def movey(self,spead):
        n=[]
        if self.moveup:
            self.nowanim='up'
            self.y-=spead
            boom=self.map.getcollideNotEffective(self.getboundbox())
            for i in boom:
                self.y=i.bottom
        if self.movedown:
            self.nowanim='down'
            self.y+=spead
            boom=self.map.getcollideNotEffective(self.getboundbox())
            for i in boom:
                self.y=i.top-self.playerphoto.get_height()
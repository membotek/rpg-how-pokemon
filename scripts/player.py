import pygame
from scripts import util,map,setings,animation
class Player:
    def __init__(self,x,y,spead,map):
        self.x=x
        self.y=y
        self.moveright=False
        self.moveleft=False
        self.moveup=False
        self.movedown=False
        self.spead=spead
        self.map=map
        self.nowanim='down'
        self.path=util.loadimage('C:/Users/Makar/new_after_test_game/maps/map.png')
        self.playerphoto=util.loadimage('C:/Users/Makar/new_after_test_game/graphics/player/down/down_0.png',1,(255,255,255))
        self.animations={
            'right':animation.Animation('C:/Users/Makar/rpg-how-pokemon/graphics/player/right',5),
            'left':animation.Animation('C:/Users/Makar/rpg-how-pokemon/graphics/player/left',5),
            'down':animation.Animation('C:/Users/Makar/rpg-how-pokemon/graphics/player/down',5),
            'up':animation.Animation('C:/Users/Makar/rpg-how-pokemon/graphics/player/up',5)
        }
    def render(self,display,camera):
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
        self.movey(self.spead)
        self.movex(self.spead)
    def getboundbox(self):
        bh=pygame.Rect(self.x,self.y,64,64)
        return(bh)
    def movex(self,spead):
        n=[]
        if self.moveright:
            self.x+=spead
            boom=self.map.getcollideNotEffective(self.getboundbox())
            for i in boom:
                self.x=i.left-self.playerphoto.get_width()
        if self.moveleft:
            self.x-=spead
            boom=self.map.getcollideNotEffective(self.getboundbox())
            for i in boom:
                self.x=i.right
    def movey(self,spead):
        n=[]
        if self.moveup:
            self.y-=spead
            boom=self.map.getcollideNotEffective(self.getboundbox())
            for i in boom:
                self.y=i.bottom
        if self.movedown:
            self.y+=spead
            boom=self.map.getcollideNotEffective(self.getboundbox())
            for i in boom:
                self.y=i.top-self.playerphoto.get_height()
import pygame,math
from scripts import util,map,setings,animation,obj,details,weapon

class Player:
    def __init__(self,x,y,spead,map):
        self.x=x
        self.y=y
        self.level=4
        self.maxhp=35*(1.25*self.level)
        self.hp=self.maxhp
        self.moveright=False
        self.moveleft=False
        self.moveup=False
        self.movedown=False
        self.fight=False
        self.nowweapons='axe'
        self.timeratack=0
        self.spead=spead
        self.inventory={}
        self.map=map
        self.basesheald=2
        self.sheald=2
        self.energy={}
        self.batlimg=util.loadimage('graphics/player/up/up_0.png',2)
        self.statue_render=util.loadimage('graphics\player\down_idle\idle_down.png',2)
        self.coldown=30
        self.bag=Bag(self.inventory)
        self.secterboundbox=None
        self.nowanim='down'
        self.path=util.loadimage('maps/map.png')
        self.playerphoto=util.loadimage('graphics/player/down/down_0.png',1,(255,255,255))
        self.listweapons={
            'axe':util.loadnameimages('graphics/weapons/axe',1)
        }
        self.animations={
            'right':animation.Animation('graphics/player/right',5),
            'left':animation.Animation('graphics/player/left',5),
            'down':animation.Animation('graphics/player/down',5),
            'up':animation.Animation('graphics/player/up',5),
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
            self.atack
        self.animations[self.nowanim].render(display,self.x-camera[0],self.y-camera[1])

    def update(self,display):
        self.animations[self.nowanim].udate()
        spead=self.spead
        self.coldown-=1
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
            self.x+=(b[0]//64*64-self.x)/10
            self.y+=(b[1]//64*64-self.y)/10
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

    def atack(self):
        if self.nowanim=='fightright':
            x=64
            y=0
            self.secterboundbox=pygame.Rect(self.x+64,self.y-64,64,3*64)
        if self.nowanim=='fightleft':
            x=-64
            y=0
            self.secterboundbox=pygame.Rect(self.x-64,self.y-64,64,3*64)
        if self.nowanim=='fightup':
            x=0
            y=-64
            self.secterboundbox=pygame.Rect(self.x-64,self.y-64,64*3,64)
        if self.nowanim=='fightdown':
            x=0
            y=64
            self.secterboundbox=pygame.Rect(self.x-64,self.y+64,64*3,64)
        return(self.x,self.y,x,y,)
    def return_energy(self):
        self.energy.clear()
        for i in weapon.GLOBALHAVEMOVMENTS[self.nowweapons]:
                if i[0] in weapon.NOWHAVEMOVMENTS.values():
                    self.energy[i[0]]=i[3]
    
class Bag:
    def __init__(self,inventory):
        self.x=100
        self.y=100
        self.w=setings.SCREAN_WIDTH-setings.SCREAN_WIDTH/1.3
        self.h=setings.SCREAN_HEIGHT-setings.SCREAN_HEIGHT/1.3
        self.inventory=inventory
        self.ficsation=[]

    def render(self,display):
        pygame.draw.rect(display,(4,4,4),(self.x,self.y,self.w,self.h))

    def update(self):
        bb=pygame.Rect(self.x,self.y,self.w,20)
        mxy=pygame.mouse.get_pos()
        mxy=list(mxy)
        mxy[0]//=setings.Scale
        mxy[1]//=setings.Scale
        if pygame.mouse.get_pressed()[0]:
            if bb.collidepoint(mxy) or self.move==True:
                self.move=True
                if len(self.ficsation)<3:
                    self.ficsation.append(self.x-mxy[0])
                    self.ficsation.append(self.y-mxy[1])
                self.x=mxy[0]+self.ficsation[0]
                self.y=mxy[1]+self.ficsation[1]
        else:
            self.move=False
            self.ficsation=[]

    def saveinventory(self,obj):
        if obj in self.inventory:
            self.inventory[obj]+=1
        else:
            self.inventory[obj]=1
            
    def show_inventory(self,display):
        font=pygame.font.Font(None,50)
        for n,i in enumerate(self.inventory):
            img=font.render(f"{i} x{self.inventory[i]}",True,(255,255,255))
            display.blit(img,(self.x+25,self.y+25+(n*60)))
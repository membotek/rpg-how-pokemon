from scripts import animation,map,util,setings
import random
import pygame

class Enemy:
    def __init__(self,x,y,spead,map,name,level,cofintcenthp=1.5,cofincentdmg=2):
        self.map=map
        self.timer=120
        self.undead=True
        self.playerphoto=util.loadimage('graphics/monsters/'+name+'/idle/0.png',1,(0,0,0))
        self.stoptimer=20
        self.breaktime=0
        self.longto=0
        self.stop=[]
        self.spead=4
        self.x=x
        self.xd=x
        self.oxiomax=x
        self.y=y
        self.yd=y
        self.oxiomay=y
        if name=='bamboo':
            self.damages=10*level//cofincentdmg
            self.maxhp=75*level//cofintcenthp
            self.batlimg=pygame.transform.scale(self.playerphoto,(self.playerphoto.get_width()*2,self.playerphoto.get_height()*2))
            self.batly=50
            self.hp=self.maxhp
            self.sheald=2
            self.attacks=[['hit',1,1],['block',1,0],['grow',4,0]
            ] # grow=upgrade sheald,   

        if name=='raccoon':
            self.damages=20*level//cofincentdmg
            self.maxhp=100*level//cofintcenthp
            self.batlimg=pygame.transform.scale(self.playerphoto,(self.playerphoto.get_width()*1.5,self.playerphoto.get_height()*1.5))
            self.batly=20
            self.hp=self.maxhp
            self.sheald=4
            self.attacks=[['hit',1,1],['block',1,0],['jump',4,2]
            ]
            
        if name=='spirit':
            self.damages=15*level//cofincentdmg
            self.maxhp=50*level//cofintcenthp
            self.batly=50
            self.hp=self.maxhp
            self.batlimg=pygame.transform.scale(self.playerphoto,(self.playerphoto.get_width()*2,self.playerphoto.get_height()*2))
            self.sheald=1
            self.attacks=[['hit',1,1,20],['block',1,0,20],['rebith of the phonex',4,0,5],['anigalation',6,3,1]
            ] 
            # rebith of the fire= self.hp*1.5
            # anigalation = self.hp*0 but self.damages*3
            
        if name=='squid':
            self.damages=10*level//cofincentdmg
            self.maxhp=100*level//cofintcenthp
            self.batly=50
            self.hp=self.maxhp
            self.batlimg=pygame.transform.scale(self.playerphoto,(self.playerphoto.get_width()*2,self.playerphoto.get_height()*2))
            self.sheald=3
            self.attacks=[['hit',1,1],['block',1,0],['splash',4,1]
            ]
            
        self.moveright=False
        self.moveleft=False
        self.moveup=False
        self.movedown=False
        self.fight=False
        self.nowanim='idle'
        self.animations={
            'move':animation.Animation('graphics/monsters/'+name+'/move',5),
            'idle':animation.Animation('graphics/monsters/'+name+'/idle',5),
            'atack':animation.Animation('graphics/monsters/'+name+'/attack',5),
            'dead':animation.Animation('graphics/monsters/'+name+'/deadmove',5)
        }
    def update(self,objects,player):
        if abs(self.x-player.x)<=setings.SCREAN_WIDTH*1.5 and abs(self.y-player.y)<=setings.SCREAN_HEIGHT*1.5:
            if self.moveright==False and self.moveleft==False and self.moveup==False and self.movedown==False:
                self.nowanim='idle'
            self.animations[self.nowanim].udate()
            self.breaktime-=1
            if self.x==self.xd and self.y==self.yd:
                self.nowanim='move'
                if self.breaktime<=0:
                    if self.undead:
                        self.ai()
            else:
                self.move(objects)
            if self.hp<=0:
                self.undead=False
                self.nowanim='dead'
                self.timer-=1
                if self.timer<=0:
                    objects.remove(self)

            

    def render(self,display,camera):
        self.animations[self.nowanim].render(display,self.x-camera[0],self.y-camera[1],self.undead)
    def ai(self):
        direction=random.randint(1,5)   # 1-top,2-right,3-down,4-left
        if direction==1:
            self.longto=random.randint(3,9)
            self.xd=self.x
            self.yd=self.y-self.longto*64
            # if abs(self.oxiomay-self.y)+longto*64<=6*64:
            self.moveup=True
            self.movedown=False
            self.moveright=False
            self.moveleft=False
        elif direction==2:
            self.longto=random.randint(3,9)
            self.xd=self.x+self.longto*64
            self.yd=self.y
            self.moveup=False
            self.movedown=False
            self.moveright=True
            self.moveleft=False
        elif direction==3:
            self.longto=random.randint(3,9)
            self.xd=self.x
            self.yd=self.y+self.longto*64
            self.moveup=False
            self.movedown=True
            self.moveright=False
            self.moveleft=False
        elif direction==4:
            self.longto=random.randint(3,9)
            self.xd=self.x-self.longto*64
            self.yd=self.y
            self.moveup=False
            self.movedown=False
            self.moveright=False
            self.moveleft=True
        elif direction==6:
            self.moveup=False
            self.movedown=False
            self.moveright=False
            self.moveleft=False
            self.nowanim='move'
            self.breaktime=self.longto*15
    def move(self,objects):
        spead=self.spead
        if (self.moveright or self.moveleft) and (self.movedown or self.moveup):
            spead/=1.41
        if self.x<=0:
            self.x=0
        if self.y<=0:
            self.y=0
        if self.moveright==False and self.moveleft==False and self.moveup==False and self.movedown==False:
            b=self.getboundbox().topleft
            self.x=b[0]//64*64
            self.y=b[1]//64*64
            if self.nowanim in ('right','left','up','down'):
                self.nowanim='idle'+self.nowanim
        self.movey(self.spead,objects)
        self.movex(self.spead,objects)
        if self.moveright==True or self.moveleft==True or self.moveup==True or self.movedown==True:
            self.stoptimer-=1
            self.stop.append((self.x,self.y))
            if self.stoptimer<=0:
                self.stoptimer=20
                if self.stop[-3]==self.stop[-2]==self.stop[-1]:
                    self.ai()
                    self.stop=[]
    def getboundbox(self):
        bh=pygame.Rect(self.x,self.y,self.animations[self.nowanim].images[0].get_width(),self.animations[self.nowanim].images[0].get_height())
        return(bh)
    def movex(self,spead,objekts):
        n=[]
        if self.moveright:
            self.nowanim='move'
            self.x+=spead
            boom=self.map.getcollideNotEffective(self.getboundbox())
            for i in boom:
                self.x=i.left-self.playerphoto.get_width()
            for i in objekts:
                if i==self:
                    continue
                a=i.getboundbox()
                b=self.getboundbox()
                if b.colliderect(a):
                    self.x=a.left-self.playerphoto.get_width()
        if self.moveleft:
            self.nowanim='move'
            self.x-=spead
            boom=self.map.getcollideNotEffective(self.getboundbox())
            for i in boom:
                self.x=i.right
            for i in objekts:
                if i==self:
                    continue
                a=i.getboundbox()
                b=self.getboundbox()
                if b.colliderect(a):
                    self.x=a.right
    def movey(self,spead,objekts):
        n=[]
        if self.moveup:
            self.nowanim='move'
            self.y-=spead
            boom=self.map.getcollideNotEffective(self.getboundbox())
            for i in boom:
                self.y=i.bottom
            for i in objekts:
                if i==self:
                    continue
                a=i.getboundbox()
                b=self.getboundbox()
                if b.colliderect(a):
                    self.y=a.bottom
        if self.movedown:
            self.nowanim='move'
            self.y+=spead
            boom=self.map.getcollideNotEffective(self.getboundbox())
            for i in boom:
                self.y=i.top-self.playerphoto.get_height()
            for i in objekts:
                if i==self:
                    continue
                a=i.getboundbox()
                b=self.getboundbox()
                if b.colliderect(a):
                    self.y=a.top-self.playerphoto.get_height()
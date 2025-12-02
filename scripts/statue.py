import pygame
from scripts import util,player,weapon,setings,widget,util
font=pygame.font.Font(None,20)
text='press(e) to use statue'
text_image=font.render(text,1,(235,235,235))
def load_icons():
    global lock
    lock=util.loadimage('graphics/icons/ChatGPT_Image_20_нояб._2025_г.__17_42_06-removebg-preview.png',0.128,(255,255,254))
class Statue:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def render(self,player,camera,display,E):
        a=pygame.rect.Rect(self.x-192,self.y-320,512,576)
        # pygame.draw.rect(display,(255,2,2),(self.x-192-camera[0],self.y-256-camera[1],512,576))
        playerbound=player.getboundbox()
        if a.colliderect(playerbound):
            display.blit(text_image,(0,0))
            if E==True:
                self.meny=Meny(player,display)
                self.meny.run()
                
class Meny:
    def __init__(self,player,display):
        self.player=player
        self.display=pygame.display.get_surface()
        self.fps=pygame.time.Clock()
        self.g=None
        self.gg=[]
        self.active=False
        self.click=False
        self.active2=False
        self.wig=[
            widget.Button(self,0.27*setings.SCREAN_WIDTH,0.12*setings.SCREAN_HEIGHT,0.15*setings.SCREAN_WIDTH,0.1*setings.SCREAN_HEIGHT,weapon.NOWHAVEMOVMENTS[1] if 1 in weapon.NOWHAVEMOVMENTS else 'nothing attack',(2,2,2),(200,200,200),(255,255,255),True),
            widget.Button(self,0.10*setings.SCREAN_WIDTH,0.41*setings.SCREAN_HEIGHT,0.15*setings.SCREAN_WIDTH,0.1*setings.SCREAN_HEIGHT,weapon.NOWHAVEMOVMENTS[2] if 2 in weapon.NOWHAVEMOVMENTS else 'nothing attack',(2,2,2),(200,200,200),(255,255,255),True),
            widget.Button(self,0.10*setings.SCREAN_WIDTH,0.24*setings.SCREAN_HEIGHT,0.15*setings.SCREAN_WIDTH,0.1*setings.SCREAN_HEIGHT,weapon.NOWHAVEMOVMENTS[3] if 3 in weapon.NOWHAVEMOVMENTS else 'nothing attack',(2,2,2),(200,200,200),(255,255,255),True),
            widget.Button(self,0.27*setings.SCREAN_WIDTH,0.52*setings.SCREAN_HEIGHT,0.15*setings.SCREAN_WIDTH,0.1*setings.SCREAN_HEIGHT,weapon.NOWHAVEMOVMENTS[4] if 4 in weapon.NOWHAVEMOVMENTS else 'nothing attack',(2,2,2),(200,200,200),(255,255,255),True),
            widget.Button(self,0.44*setings.SCREAN_WIDTH,0.41*setings.SCREAN_HEIGHT,0.15*setings.SCREAN_WIDTH,0.1*setings.SCREAN_HEIGHT,weapon.NOWHAVEMOVMENTS[5] if 5 in weapon.NOWHAVEMOVMENTS else 'nothing attack',(2,2,2),(200,200,200),(255,255,255),True),
            widget.Button(self,0.44*setings.SCREAN_WIDTH,0.24*setings.SCREAN_HEIGHT,0.15*setings.SCREAN_WIDTH,0.1*setings.SCREAN_HEIGHT,weapon.NOWHAVEMOVMENTS[6] if 6 in weapon.NOWHAVEMOVMENTS else 'nothing attack',(2,2,2),(200,200,200),(255,255,255),True)
        ]
        for i in self.wig:
            i.slot2=self.resetactive

    def render(self):
        self.display.fill([0,0,0])
        pygame.draw.rect(self.display,(15,15,15),(setings.SCREAN_WIDTH*2//3,0,setings.SCREAN_WIDTH//3,setings.SCREAN_HEIGHT))
        self.display.blit(self.player.statue_render,(setings.SCREAN_WIDTH*2//6.5,setings.SCREAN_HEIGHT//3))
        for i in self.gg:
            i.render()
        for i in self.wig:
            i.render(self.display)
            i.update()
        
    def resetactive(self):
        self.active=False
    def run(self):
        x=setings.SCREAN_WIDTH*2//3+25
        y=0
        for h in weapon.GLOBALHAVEMOVMENTS.values():
            for i in h:
                self.g=TEXT_OF_MOVEMENTS(x,y,i[0],self.display,self,self.player)
                self.gg.append(self.g)
                y+=self.g.text.get_height()*1.3
        while True:
            self.render()
            pygame.display.update()
            self.fps.tick(60)
            self.click=False
            for i in pygame.event.get():
                if i.type==pygame.QUIT:
                    exit(0)
                if i.type==pygame.KEYDOWN:
                    if i.key==pygame.K_e:
                        return()
                if i.type==pygame.MOUSEBUTTONDOWN:
                    self.click=True
                if i.type==pygame.MOUSEWHEEL:
                    if self.gg[0].y<0:
                        if i.y==1:
                            for b in self.gg:
                                b.y+=0.2*setings.SCREAN_HEIGHT
                    if i.y==-1:
                        for b in self.gg:
                            b.y-=0.1*setings.SCREAN_HEIGHT
            if self.active and self.active2:
                    if self.active2.name not in weapon.NOWHAVEMOVMENTS.values():
                        if self.active2.level<self.player.level:
                            self.active.changetext(self.active2.name)
                            self.active.orgtext=self.active2.name
                            weapon.NOWHAVEMOVMENTS[self.wig.index(self.active)+1]=self.active2.name
                            self.active2=False
                            self.active=False
                        else:
                            self.active2=False
                            self.active=False
                    else:
                        self.active2=False
                        self.active=False
class TEXT_OF_MOVEMENTS:
    def __init__(self,x,y,name,display,menu,player):
        self.x=x
        self.y=y
        self.name=name
        self.player=player
        self.w=len(self.name)*5
        self.font=pygame.font.Font(None,75)
        self.text=self.font.render(self.name,True,(225,255,255))
        self.display=display
        self.menu=menu
        for i in weapon.GLOBALHAVEMOVMENTS['axe']:
            if self.name==i[0]:
                self.level=i[1]

    def render(self):
        rect=self.display.blit(self.text,(self.x,self.y))
        if rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.display,(200,200,200),(rect.left,rect.bottom,rect.width,7))
            if self.menu.click==True:
                if self.menu.active2==self:
                    self.menu.active2=False
                else:
                    self.menu.active2=self
        if self.menu.active2==self:
            pygame.draw.rect(self.display,(200,200,200),(rect.left,rect.bottom,rect.width,7))
        if self.level>self.player.level:
            self.display.blit(lock,(rect.right+10,rect.top-16))
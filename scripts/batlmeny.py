import pygame
from scripts import widget,util,setings,weapon,fightbrain
full=True

def drawhp(maxhp,hp,cords,color,display):
    pygame.draw.rect(display,(230,0,0),(cords[0],cords[1],setings.SCREAN_WIDTH//6,setings.SCREAN_HEIGHT//40),0,7)
    pygame.draw.rect(display,(0,188,0),(cords[0],cords[1],(hp*setings.SCREAN_WIDTH//6)//maxhp,setings.SCREAN_HEIGHT//40),0,7)


class BaseMenu:

    def __init__(self, x, y, width, height, title):
        self.x = x
        self.y = y
        self.click=False
        self.width = width
        self.height = height
        self.title = title

    def render(self, display):
        pygame.draw.rect(display, (255, 255, 255), (self.x, self.y, self.width, self.height),)
        for button in self.buttons:
            button.render(display)

    def update(self):
        for button in self.buttons:
            button.update()


class Meny(BaseMenu):

    def __init__(self, x, y, width, height, title):
        super().__init__(x,y,width,height,title)
        self.retturn=False
        self.stated = 'Attack'
        w = setings.SCREAN_WIDTH / 7
        h = setings.SCREAN_HEIGHT / 20
        self.buttons = [
            widget.Button(self,x//3, y, w, h, 'attack', color=(0, 128, 0), hovercolor=(125, 125, 125)),
            widget.Button(self,x//3, y + h+5, w, h, 'items', color=(128, 0, 0), hovercolor=(125, 125, 125)),
            widget.Button(self,x//3, y + h * 2+10, w, h, 'run away', color=(0, 128, 128), hovercolor=(125, 125, 125))
        ]
        self.active=None
        self.attackinermenu = AttackInnerMenu(self, w, y, w, h,'lol', 'axe')
    
    def hendelattack(self,button: widget.Button):
        damage=fightbrain.calcutedamage(self.weapon, button.text, None, self.enemy, self.player)
        self.enemy.hp-=damage
        if self.enemy.hp<0:
            return

    def render(self, display):
        super().render(display)
        self.renderctent(display)
        if self.active==self.buttons[0]:
            self.attackinermenu.render(display)
   
    def renderctent(self, display):
        # self.enemy.animations[self.enemy.nowanim].render(display,0,0)
        display.blit(self.enemy.batlimg,(setings.SCREAN_WIDTH/2.5-self.enemy.batlimg.get_width()/2,self.enemy.batly))
        display.blit(self.player.batlimg,(setings.SCREAN_WIDTH//4.6,self.y-self.player.batlimg.get_height()-30))
    
    def update(self):
        super().update()
        if self.active==self.buttons[0]:
            self.attackinermenu.update()

    def run(self,display,clock,maindisplay,enemy,player):
        global full
        self.retturn=False
        self.enemy=enemy
        self.player=player
        self.weapon = self.player.nowweapons
        while True:
            if self.retturn==True:
                return
            clock.tick(60)
            display.fill((0,0,0))
            self.update()
            self.render(display)
            drawhp(player.maxhp,player.hp,(setings.SCREAN_WIDTH//3-setings.SCREAN_WIDTH//36,setings.SCREAN_HEIGHT/3-setings.SCREAN_HEIGHT//18),None,display)
            drawhp(enemy.maxhp,enemy.hp,(0+setings.SCREAN_WIDTH//36,0+setings.SCREAN_HEIGHT//40),None,display)
            self.click=False
            self.attackinermenu.click = False
            for i in pygame.event.get():
                if i.type==pygame.QUIT:
                    exit(0)
                if i.type==pygame.KEYDOWN:
                    if i.key==pygame.K_b:
                        full=not full
                        if full==True:
                            setings.SCREAN_WIDTH=maindisplay.get_width()
                            setings.SCREAN_HEIGHT=maindisplay.get_height()
                            maindisplay=pygame.display.set_mode((setings.SCREAN_WIDTH,setings.SCREAN_HEIGHT),pygame.FULLSCREEN)
                            setings.SCREAN_WIDTH=maindisplay.get_width()
                            setings.SCREAN_HEIGHT=maindisplay.get_height()
                            display=pygame.Surface((setings.SCREAN_WIDTH//setings.Scale,setings.SCREAN_HEIGHT//setings.Scale))
                        if full==False:
                            setings.SCREAN_WIDTH=maindisplay.get_width()-30
                            setings.SCREAN_HEIGHT=maindisplay.get_height()-30
                            maindisplay=pygame.display.set_mode((setings.SCREAN_WIDTH,setings.SCREAN_HEIGHT))
                            setings.SCREAN_WIDTH=maindisplay.get_width()
                            setings.SCREAN_HEIGHT=maindisplay.get_height()
                            display=pygame.Surface((setings.SCREAN_WIDTH//setings.Scale,setings.SCREAN_HEIGHT//setings.Scale))
                if i.type==pygame.MOUSEBUTTONDOWN:
                    self.click=True
                    self.attackinermenu.click = True

            d=pygame.transform.scale(display,(setings.SCREAN_WIDTH,setings.SCREAN_HEIGHT))
            maindisplay.blit(d,(0,0))
            pygame.display.update()

class AttackInnerMenu(BaseMenu):

    def __init__(self, mainmenu: Meny, x, y, width, height, title, weapon):
        self.mainmenu = mainmenu
        self.active=None
        BaseMenu.__init__(self,x,y,width,height,title)
        self.x=x
        self.y=y
        self.buttons = []
        self.weapon=weapon

    def update(self):
       self.buttons=self.buttons
       super().update()

    def refresh(self):
        w = self.width / 2 
        h = setings.SCREAN_HEIGHT / 20
        for i in weapon.NOWHAVEMOVMENTS:
            if i%2==1:
                self.buttons.append(widget.Button(self,self.x + 10, self.y+i//2*h+5*i//2, w, h, weapon.NOWHAVEMOVMENTS[i], color=(0, 128, 0), hovercolor=(125, 125, 125)))
            else:
                self.buttons.append(widget.Button(self,self.x+ w + 30, self.y+(i-1)//2*h+5*(i-1)//2, w, h, weapon.NOWHAVEMOVMENTS[i], color=(0, 128, 0), hovercolor=(125, 125, 125)))
            self.buttons[-1].slot = lambda btn=self.buttons[-1]: self.mainmenu.hendelattack(btn)
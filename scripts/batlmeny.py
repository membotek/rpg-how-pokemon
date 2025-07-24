import pygame
from scripts import widget,util,setings
full=True
class Meny:
    def __init__(self, x, y, width, height, title):
        self.x = x
        self.y = y
        self.click=False
        self.width = width
        self.height = height
        self.title = title
        self.retturn=False
        self.stated = 'Attack'
        self.buttons = [
            widget.Button(self,x//3, y, 700//3, 200//3, 'attack', color=(0, 128, 0), hovercolor=(125, 125, 125)),
            widget.Button(self,x//3, y + 200//3+5, 700//3, 200//3, 'items', color=(128, 0, 0), hovercolor=(125, 125, 125)),
            widget.Button(self,x//3, y + 400//3+10, 700//3, 200//3, 'run away', color=(0, 128, 128), hovercolor=(125, 125, 125))
        ]
        self.active=None

    def render(self, display):
        pygame.draw.rect(display, (255, 255, 255), (self.x, self.y, self.width, self.height),)
        for button in self.buttons:
            button.render(display)
        self.renderctent(display)
       
    def renderctent(self, display):
        self.enemy.animations[self.enemy.nowanim].render(display,0,0)
        # self.enemy.animations[self.enemy.nowanim].render(display,setings.SCREAN_WIDTH-self.enemy.playerphoto.get_width()*1.5,20)
    def update(self):
        for button in self.buttons:
            button.update()
    def run(self,display,clock,maindisplay,enemy):
        global full
        self.retturn=False
        self.enemy=enemy
        while True:
            if self.retturn==True:
                return
            clock.tick(60)
            display.fill((0,0,0))
            self.update()
            self.render(display)
            self.click=False
            for i in pygame.event.get():
                if i.type==pygame.QUIT:
                    exit(0)
                if i.type==pygame.KEYDOWN:
                    if i.key==pygame.K_F11:
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
            d=pygame.transform.scale(display,(setings.SCREAN_WIDTH,setings.SCREAN_HEIGHT))
            maindisplay.blit(d,(0,0))
            pygame.display.update()
class AttackInnerMenu(Meny):
   def __init__(self, x, y, width, height, title):
        Meny.__init__(self,x,y,width,height,title)
        self.buttons = [
            widget.Button(self,x//3, y, 700//3, 200//3, 'attack', color=(0, 128, 0), hovercolor=(125, 125, 125)),
            widget.Button(self,x//3, y + 200//3+5, 700//3, 200//3, 'items', color=(128, 0, 0), hovercolor=(125, 125, 125)),
            widget.Button(self,x//3, y + 400//3+10, 700//3, 200//3, 'run away', color=(0, 128, 128), hovercolor=(125, 125, 125))
        ]
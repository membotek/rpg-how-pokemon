import pygame
from scripts import widget,util,setings
full=True
class Meny:
    def __init__(self, x, y, width, height, title):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.title = title
        self.stated = 'Attack'
        self.buttons = [
            widget.Button(x, y, 50, 200, 'graphics/icons/shield.png', color=(0, 128, 0), hovercolor=(255, 0, 0)),
            widget.Button(x, y + 200, 50, 200, 'graphics/icons/shield.png', color=(128, 0, 0), hovercolor=(255, 0, 0)),
            widget.Button(x, y + 400, 50, 200, 'graphics/icons/shield.png', color=(0, 128, 128), hovercolor=(255, 255, 255))
        ]

    def render(self, display):
        pygame.draw.rect(display, (0, 0, 0), (self.x*0, self.y*0, self.width, self.height), 2)
        for button in self.buttons:
            button.render(display)
    def update(self):
        for button in self.buttons:
            button.update()
    def run(self,display,clock,maindisplay):
        global full
        while True:
            clock.tick(60)
            display.fill((255,0,0))
            self.update()
            self.render(display)
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
            d=pygame.transform.scale(display,(setings.SCREAN_WIDTH,setings.SCREAN_HEIGHT))
            maindisplay.blit(d,(0,0))
            pygame.display.update()
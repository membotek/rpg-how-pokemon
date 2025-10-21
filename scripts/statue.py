import pygame
from scripts import util,player,weapon,setings
font=pygame.font.Font(None,20)
text='press(e) to use statue'
text_image=font.render(text,1,(235,235,235))
class Statue:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def render(self,player,camera,display,E):
        a=pygame.rect.Rect(self.x-192,self.y-320,512,576)
        pygame.draw.rect(display,(255,2,2),(self.x-192-camera[0],self.y-256-camera[1],512,576))
        playerbound=player.getboundbox()
        if a.colliderect(playerbound):
            display.blit(text_image,(0,0))
            if E==True:
                self.meny=Meny(player,display)
                self.meny.run()
                E=False
class Meny:
    def __init__(self,player,display):
        self.player=player
        self.display=pygame.display.get_surface()
        self.fps=pygame.time.Clock()
    def render(self):
        self.display.fill([0,0,0])
        pygame.draw.rect(self.display,(15,15,15),(setings.SCREAN_WIDTH*2//3,0,setings.SCREAN_WIDTH//3,setings.SCREAN_HEIGHT))
    def run(self):
        while True:
            self.render()
            pygame.display.update()
            self.fps.tick(60)
            for i in pygame.event.get():
                if i.type==pygame.QUIT:
                    exit(0)
                if i.type==pygame.KEYDOWN:
                    if i.key==pygame.K_SPACE:
                        return()
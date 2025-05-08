import pygame
pygame.init()
from scripts import setings,player,map
maindisplay=pygame.display.set_mode((setings.SCREAN_WIDTH,setings.SCREAN_HEIGHT))
display=pygame.Surface((setings.SCREAN_WIDTH//setings.Scale,setings.SCREAN_HEIGHT//setings.Scale))
clock=pygame.time.Clock()
map=map.Map()
mainplayer=player.Player(0,0,10,map)
while True:
    clock.tick(60)
    display.fill((0,0,0))
    mainplayer.update(display)
    map.render(display)
    mainplayer.render(display,map.camera)
    map.camera[0]+=(mainplayer.x-setings.SCREAN_WIDTH//setings.Scale//2-map.camera[0])/30
    map.camera[1]+=(mainplayer.y-setings.SCREAN_HEIGHT//setings.Scale//2-map.camera[1])/30
    for i in pygame.event.get():
            if i.type==pygame.QUIT:
                exit(0)
            if i.type==pygame.KEYDOWN:
                if i.key==pygame.K_d:
                    mainplayer.moveright=True
                if i.key==pygame.K_a:
                    mainplayer.moveleft=True
                if i.key==pygame.K_w:
                    mainplayer.moveup=True
                if i.key==pygame.K_s:
                    mainplayer.movedown=True
            if i.type==pygame.KEYUP:
                if i.key==pygame.K_d:
                    mainplayer.moveright=False
                if i.key==pygame.K_a:
                    mainplayer.moveleft=False
                if i.key==pygame.K_w:
                    mainplayer.moveup=False
                if i.key==pygame.K_s:
                    mainplayer.movedown=False
    d=pygame.transform.scale(display,(setings.SCREAN_WIDTH,setings.SCREAN_HEIGHT))
    maindisplay.blit(d,(0,0))
    pygame.display.update()
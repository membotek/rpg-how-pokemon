import pygame
pygame.init()
from scripts import setings,player,map,obj,util
import enemy
maindisplay=pygame.display.set_mode((setings.SCREAN_WIDTH,setings.SCREAN_HEIGHT))
display=pygame.Surface((setings.SCREAN_WIDTH//setings.Scale,setings.SCREAN_HEIGHT//setings.Scale))
clock=pygame.time.Clock()
map=map.Map()
mainplayer=player.Player(0,0,10,map)
enemescords=util.loadenemyfromcsv('maps/border_Tile Layer 1_enemy.csv')
print(len(enemescords))
enemes=[]
for i in enemescords:
    b=enemy.Enemy(i[0]*64,i[1]*64,1,map,i[2])
    enemes.append(b)
while True:
    clock.tick(60)
    display.fill((0,0,0))
    mainplayer.update(display)
    map.render(display,mainplayer)
    mainplayer.render(display,map.camera)
    map.renderforest(display)
    for i in enemes:
        i.render(display,map.camera)
    for i in map.objects:
        map.objects[i].render(display,map.camera,mainplayer)
        map.objects[i].update()
    map.camera[0]+=(mainplayer.x-setings.SCREAN_WIDTH//setings.Scale//2-map.camera[0])/15
    map.camera[1]+=(mainplayer.y-setings.SCREAN_HEIGHT//setings.Scale//2-map.camera[1])/15
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
            if i.type==pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]==True:
                    mainplayer.timeratack=15
                    mainplayer.fight=True
    d=pygame.transform.scale(display,(setings.SCREAN_WIDTH,setings.SCREAN_HEIGHT))
    maindisplay.blit(d,(0,0))
    pygame.display.update()
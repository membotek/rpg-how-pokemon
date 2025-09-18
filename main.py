import pygame
from scripts import setings,player,map,obj,util,details,batlmeny,weapon
import enemy

pygame.init()

maindisplay=pygame.display.set_mode((setings.SCREAN_WIDTH,setings.SCREAN_HEIGHT),pygame.FULLSCREEN)
setings.SCREAN_WIDTH=maindisplay.get_width()
setings.SCREAN_HEIGHT=maindisplay.get_height()
display=pygame.Surface((setings.SCREAN_WIDTH//setings.Scale,setings.SCREAN_HEIGHT//setings.Scale))
setings.surf = display
clock=pygame.time.Clock()
batlmeny=batlmeny.Meny(0,setings.SCREAN_HEIGHT*1/3,setings.SCREAN_WIDTH//setings.Scale,setings.SCREAN_HEIGHT//setings.Scale/3,'Battle Menu')
map=map.Map()
inventory=False
full=True
mainplayer=player.Player(0,0,10,map)
weapon.setupatack('axe',mainplayer.level,batlmeny)
enemescords=util.loadenemyfromcsv('maps/border_Tile Layer 1_enemy.csv')
enemes: list[enemy.Enemy]=[]
popkorn=[]

for i in enemescords:
    b=enemy.Enemy(i[0]*64,i[1]*64,1,map,i[2])
    enemes.append(b)

detailslist=details.loaddetailsfromscv('maps/border_Tile Layer 1_details.csv',mainplayer)

while True:
    pygame.display.set_caption(str(len(enemes)))
    clock.tick(60)
    display.fill((0,0,0))
    mainplayer.update(display)
    if mainplayer.fight==True:
        for i in detailslist:
            i.anigelastion(popkorn,detailslist)
    map.render(display,mainplayer)
    for i in detailslist:
        i.render(display,map.camera)
    mainplayer.render(display,map.camera)
    map.renderforest(display)
    for i in enemes:
        i.render(display,map.camera)
        i.update(enemes)
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
                # if i.key==pygame.K_F11:
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
                        setings.SCREAN_WIDTH=maindisplay.get_width()*0.5
                        setings.SCREAN_HEIGHT=maindisplay.get_height()*0.5
                        maindisplay=pygame.display.set_mode((setings.SCREAN_WIDTH,setings.SCREAN_HEIGHT))
                        setings.SCREAN_WIDTH=maindisplay.get_width()
                        setings.SCREAN_HEIGHT=maindisplay.get_height()
                        display=pygame.Surface((setings.SCREAN_WIDTH//setings.Scale,setings.SCREAN_HEIGHT//setings.Scale))
                if i.key==pygame.K_i:
                    inventory=not inventory
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
                    if mainplayer.coldown<=0:
                        mainplayer.timeratack=15
                        mainplayer.fight=True
                        mainplayer.coldown=30
                        for i in enemes:
                            if mainplayer.getboundbox().colliderect(i.getboundbox()):
                                mainplayer.moveright=False
                                mainplayer.moveleft=False
                                mainplayer.moveup=False
                                mainplayer.movedown=False
                                batlmeny.run(display,clock,maindisplay,i,mainplayer)
    if inventory==True:
        mainplayer.bag.render(display)
        mainplayer.bag.update()
        mainplayer.bag.show_inventory(display)
    for i in popkorn:
        i.render(display,map.camera)
        i.update(popkorn)
    d=pygame.transform.scale(display,(setings.SCREAN_WIDTH,setings.SCREAN_HEIGHT))
    maindisplay.blit(d,(0,0))
    pygame.display.update()
import pygame
from scripts import setings,player,map,obj,util,details,batlmeny,weapon,statue,dialoge,share
import enemy

pygame.init()
font=pygame.font.Font(None,50)
smalfont=pygame.font.Font(None,28)
maindisplay=pygame.display.set_mode((setings.SCREAN_WIDTH,setings.SCREAN_HEIGHT),pygame.FULLSCREEN)
setings.SCREAN_WIDTH=maindisplay.get_width()
setings.SCREAN_HEIGHT=maindisplay.get_height()
display=pygame.Surface((setings.SCREAN_WIDTH//setings.Scale,setings.SCREAN_HEIGHT//setings.Scale))
setings.surf = display
dialog_dkrean=pygame.Surface(display.get_size(),pygame.SRCALPHA)
clock=pygame.time.Clock()
batlmeny=batlmeny.Meny(0,setings.SCREAN_HEIGHT*1/3,setings.SCREAN_WIDTH//setings.Scale,setings.SCREAN_HEIGHT//setings.Scale/3,'Battle Menu')
map=map.Map()
inventory=False
full=True
mainplayer=player.Player(0,0,10,map)
share.mainplayer=mainplayer
weapon.setupatack('axe',mainplayer.level,batlmeny)
mainplayer.return_energy()
enemescords=util.loadenemyfromcsv('maps/border_Tile Layer 1_enemy.csv')
enemes: list[enemy.Enemy]=[]
popkorn=[]
E=None
DEBAG=True
indialog=None
statue.load_icons()
answers=[]
click=False
Lester=enemy.Lester(0,0,124,map,mainplayer.level)
Boby=enemy.NPC(240,0,124,map,mainplayer.level,"boby")
enemes.insert(0,Lester)
enemes.insert(0,Boby)

for i in enemescords:
    b=enemy.Enemy(i[0]*64,i[1]*64,1,map,i[2],mainplayer.level)
    enemes.append(b)

detailslist=details.loaddetailsfromscv('maps/border_Tile Layer 1_details.csv',mainplayer)
statues=util.loadobjfromcsv('maps/border_Tile Layer 1_objects.csv')
statueas=[]
for i in statues:
        statuea=statue.Statue(i[0]*64,i[1]*64)
        statueas.append(statuea)
text_e='press "E".'
text_image=smalfont.render(text_e,1,(250,250,250))
dialog_manager=dialoge.Dialogmanager()
def change_dialog_state():
    global d_text,answers,indialog
    if dialog_manager.checkpoint=='End':
        indialog=False
        answers=[]
    else:
        d_text=dialoge.Dialog_text(dialog_manager.gettext())
        answers=[]
while True:
    pygame.display.set_caption(str(len(enemes)))
    clock.tick(60)
    display.fill((0,0,0))
    mainplayer.update(display)
    if mainplayer.fight==True:
        for i in detailslist:
            i.anigelastion(popkorn,detailslist)
    map.render(display,mainplayer)
    eria=mainplayer.detect_eria()
    for i in detailslist:
        i.render(display,map.camera)
    mainplayer.render(display,map.camera)
    map.renderforest(display)
    for i in statueas:
        i.render(mainplayer,map.camera,display,E)
    for i in enemes:
        i.render(display,map.camera)
        i.update(enemes,mainplayer)
        if eria.colliderect(i.getboundbox()):
            display.blit(text_image,(10,10))
            if E==True:
                indialog=True
                dialog_manager.startdialog(i.name)
                d_text=dialoge.Dialog_text(dialog_manager.gettext())
                name_text=dialoge.Dialog_text(i.name,x=setings.SCREAN_WIDTH*0.05,y=setings.SCREAN_HEIGHT*0.27,font_size=60,text_colour=(250,250,250))
                i.indialog=True
            if indialog==False:
                i.indialog=False
    if indialog==True:
        dialog_dkrean.fill((0,0,0,100))
        pygame.draw.rect(dialog_dkrean,(201,148,42,252),(setings.SCREAN_WIDTH//25,setings.SCREAN_HEIGHT//3-25,setings.SCREAN_WIDTH//2.4,setings.SCREAN_HEIGHT//3),0,10)
        d_text.update()
        d_text.render(dialog_dkrean)
        name_text.update()
        name_text.render(dialog_dkrean)
        if d_text.finished()==True and answers==[]:
                    textss=dialog_manager.getchoises()
                    for pos,n in enumerate(textss):
                        answers.append(dialoge.Dialog_answers(n['text'],n['next'],x=setings.SCREAN_WIDTH*0.05,y=setings.SCREAN_HEIGHT*0.42+pos*42,))
        for m in answers:
            m.render(dialog_dkrean)
            m.update()
            m.answers_update(dialog_dkrean,click,dialog_manager,change_dialog_state)
    for i in map.objects:
        map.objects[i].render(display,map.camera,mainplayer)
        map.objects[i].update()
    map.camera[0]+=(mainplayer.x-setings.SCREAN_WIDTH//setings.Scale//2-map.camera[0])/15
    map.camera[1]+=(mainplayer.y-setings.SCREAN_HEIGHT//setings.Scale//2-map.camera[1])/15
    click=False
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
                if i.key==pygame.K_e:
                    E=True
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
                if i.key==pygame.K_e:
                    E=False
            if i.type==pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]==True:
                    click=True
                    if mainplayer.coldown<=0:
                        mainplayer.timeratack=15
                        if indialog==False:
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
    if DEBAG==True:
        xy=pygame.mouse.get_pos()
        mx=int(xy[0]/setings.SCREAN_WIDTH*100)
        my=int(xy[1]/setings.SCREAN_HEIGHT*100)
        w=font.render(str(mx),1,(255,255,255))
        h=font.render(str(my),1,(255,255,255))
        display.blit(w,(0,0))
        display.blit(h,(0,50))
        

    if indialog==True:
        display.blit(dialog_dkrean,(0,0))
    d=pygame.transform.scale(display,(setings.SCREAN_WIDTH,setings.SCREAN_HEIGHT))
    maindisplay.blit(d,(0,0))
    pygame.display.update()
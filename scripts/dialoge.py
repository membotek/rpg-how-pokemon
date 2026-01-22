import os, json, pygame
from scripts import setings, queat, share
dialogs={}
def load_dialogs():
    Filenames=os.listdir('dialogs')
    for i in Filenames:
        f=open("dialogs/"+i)
        dialog=json.load(f)
        f.close()
        dialogs[i[:-5]]=dialog
load_dialogs()

class Dialogmanager:
    def __init__(self):
        self.checkpoint='start'
        self.optionid=0
        self.dialog=None

    def startdialog(self,withwho):
        self.dialog=dialogs[withwho]
        self.checkpoint=self.dialog["Meta"]["start"]
        self.optionid=0

    def check_action(self):
        a=self.dialog[self.checkpoint]["choices"][self.optionid]
        if "action" in a :
            if a["action"] == "create quest":
                queat.quest_active.append(queat.Quest(a["quest type"],a["quest goal"],a["quest from"]))
        if "action" in a :
            if a["action"] == "full hp":
                share.mainplayer.hp=share.mainplayer.maxhp
        if "action" in a :
            if a["action"] == "finish quest":
                share.mainplayer.nowxp+=a["exp"]
        if "meta action" in a:
            self.dialog["Meta"]["start"]=a["meta action"]
        if share.mainplayer.nowxp >= share.mainplayer.level2xp[share.mainplayer.level]:
            for i in share.mainplayer.level2xp:
                if share.mainplayer.level2xp[i] <= share.mainplayer.nowxp < share.mainplayer.level2xp[i+1]:
                    share.mainplayer.level=i
            print("ok")
        print(share.mainplayer.level)
    def gettext(self):
        a=self.dialog[self.checkpoint]['text']
        return(a)
    
    def getchoises(self):
        b=self.dialog[self.checkpoint]['choices']
        texts=[]
        for i in b:
            texts.append(i)
        return(texts)
    
    def change_state(self,state):
        self.check_action()
        self.checkpoint=state
class Dialog_text:
    def __init__(self,text,period=3,text_colour=(245,245,245),font_size=42,font_name=None,x=setings.SCREAN_WIDTH*0.05,y=setings.SCREAN_HEIGHT*0.34): 
        self.text=text
        self.period=period
        self.text_colour=text_colour
        self.font=pygame.font.Font(font_name,font_size)
        self.index=0
        self.timer=period
        self.x=x
        self.y=y
    def update(self):
        self.timer-=1
        if self.timer<=0:
            self.timer=self.period
            self.index+=1
            if self.index>len(self.text)-1:
                self.index-=1
    def render(self,display):
        f=self.font.render(self.text[0:self.index+1],True,self.text_colour)
        display.blit(f,(self.x,self.y))
    def finished(self):
        if self.index==len(self.text)-1:
            return(True)
        else:
            return(False)
class Dialog_answers(Dialog_text):
    def __init__(self, text, next, period=3, text_colour=(245, 245, 245), font_size=42, font_name=None, x=setings.SCREAN_WIDTH * 0.05, y=setings.SCREAN_HEIGHT * 0.34):
        super().__init__(text, period, text_colour, font_size, font_name, x, y)
        f=self.font.render(self.text,True,self.text_colour)
        self.bound=pygame.rect.Rect(self.x,self.y,f.get_width(),f.get_height())
        self.next=next
    def answers_update(self,display,click,dialogmaneger,change_dialog_state):
        xy=pygame.mouse.get_pos()
        xy=[xy[0]//2,xy[1]//2]
        if self.bound.collidepoint(xy):
            pygame.draw.rect(display,(self.text_colour),(self.x,self.bound.bottom,self.bound.width,3.5))
            if click==True:
                dialogmaneger.change_state(self.next)
                change_dialog_state()
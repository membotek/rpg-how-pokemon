from scripts import util
class Animation:
    def __init__(self,path,fps,scale=1):
        self.images=util.loadimages(path,scale)
        self.nomber=0
        self.fps=fps
        self.ofps=self.fps
        # old
        
    def render(self,display,x,y):
        display.blit(self.images[self.nomber],(x,y))

    def udate(self):
        self.fps-=1
        if self.fps<=0:
            self.nomber+=1
            self.fps=self.ofps
            if self.nomber==len(self.images):
                self.nomber=0
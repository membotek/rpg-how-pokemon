from scripts import animation
class Enemy:
    def __init__(self,x,y,spead,map,name):
        self.x=x
        self.y=y
        self.moveright=False
        self.moveleft=False
        self.moveup=False
        self.movedown=False
        self.fight=False
        self.nowanim='idle'
        self.animations={
            'move':animation.Animation('graphics/monsters/'+name+'/move',5),
            'idle':animation.Animation('graphics/monsters/'+name+'/idle',5),
            'atack':animation.Animation('graphics/monsters/'+name+'/attack',5),
        }
    def update(self):
        if self.moveright==False and self.moveleft==False and self.moveup==False and self.movedown==False:
            self.nowanim='idle'
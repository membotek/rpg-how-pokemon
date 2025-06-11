from scripts import util
class Detail:
    def __init__(self,x,y,id):
        self.x=x
        self.y=y
        if 0<=id<=15:
            ids=[id,0]
            util.slise('graphics/tilemap/details.png',nomber=ids)
        if 16<=id==16:
            ids=[0,1]
            util.slise('graphics/tilemap/details.png',nomber=ids)
        if 32<=id==39:
            ids=[id-32,2]
            util.slise('graphics/tilemap/details.png',nomber=ids)
        if 48==55:
            ids=[id-48,3]
            util.slise('graphics/tilemap/details.png',nomber=ids)
        
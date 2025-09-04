DAMAGES={
    'axe':30,
    'lance':10,
    'rapier':20,
    'sai':10,
    'sword':15
}
NOWHAVEMOVMENTS={
    1:'hit1',
    2:'hit2',
    3:'hit3',
    4:'hit4',
    5:'hit5',
    6:'hit6',
}
GLOBALHAVEMOVMENTS={
    'axe':[['hit',1,0.5],['crushing attack',2,2],['block',1,0]],     # weapon:['atackname,(open level)',cofincent]
    'lance':[['hit',1],['block',1]],
    'rapier':[['hit',1],['block',1]],
    'sai':[['hit',1],['block',1]],
    'sword':['hit','cutting attack','block'],
}
def setupatack(weapon,level,batlmany):
    NOWHAVEMOVMENTS.clear()
    q=1
    for i in GLOBALHAVEMOVMENTS[weapon]:
        if i[1]<=level:
            NOWHAVEMOVMENTS[q]=i[0]
            q+=1
            if q==7:
                return
    batlmany.attackinermenu.refresh()
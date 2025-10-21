import pygame
from scripts import weapon
import random
def calcutedamage(weaponname,platackname,enemy,player,lastenatackname=None):  # attack to enemy
    damage=weapon.DAMAGES[weaponname]
    if lastenatackname=='block':
        damage*=0.5
    for i in weapon.GLOBALHAVEMOVMENTS[weaponname]:
        if i[0]==platackname:
            damage*=i[2]
    a=random.randint(1,100)
    if a<=5:   # 5% crit
        damage*=2
    elif 6<=a<=95:   # 90% normal
        damage*=1
    elif a>=96:   # 5% lose
        damage*=0.5
    damage/=enemy.sheald/2
    damage*=player.level/4
    return (damage)
def enemycalcutedamage(enatackname,lastplatackname,player,enemy):  # attavk to player
    damage=enemy.damages
    if lastplatackname=='perfect block':
        damage*=0.5
    for i in enemy.attacks:
        if i[0]==enatackname:
            damage*=i[2]
    a=random.randint(1,100)
    if a<=5:   # 5% crit
        damage*=0.5
    elif 6<=a<=95:   # 90% normal
        damage*=1
    elif a>=96:   # 5% lose
        damage*=2
    damage/=player.sheald/2
    damage*=player.level/4
    return (damage)
def checkattack(enatackname,enemy,player):
    if enatackname == 'grow':
        enemy.sheald+=1
    if enatackname == 'rebith of the fire':
        enemy.hp=min(int(enemy.hp*1.5),enemy.maxhp)
    if enatackname=='anigalation':
        enemy.hp=0 
def enemy_ai_attack(player,enemy,lastplatackname=None):
    if lastplatackname=='perfect block':
        while True:
            a=random.randint(1,100)
            if a<=30:
                conddidans=[at[0] for at in enemy.attacks if at[2]==1]
                b=random.choice(conddidans)
                return(b)
            elif 30<a<50:
                conddidans=[at[0] for at in enemy.attacks if at[2]>=2]
                if conddidans==[]:
                    continue
                b=random.choice(conddidans)
                return(b)
            else:
                conddidans=[at[0] for at in enemy.attacks if at[2]==0]
                b=random.choice(conddidans)
                return(b)
    elif enemy.hp<=enemy.maxhp//100:
        a=random.randint(1,100)
        if a<=30:
            return('anigalation')
        else:
            conddidans=[at[0] for at in enemy.attacks if at[2]>0]
            b=random.choice(conddidans)
            return(b)
    else:
        while True:
            a=random.randint(1,100)
            if a<=60:
                conddidans=[at[0] for at in enemy.attacks if at[2]==1]
                b=random.choice(conddidans)
                return(b)
            elif 60<a<89:
                conddidans=[at[0] for at in enemy.attacks if at[2]==2]
                if conddidans==[]:
                    continue
                b=random.choice(conddidans)
                return(b)
            elif 89<a<90:
                conddidans=[at[0] for at in enemy.attacks if at[2]==3]
                if conddidans==[]:
                    continue
                b=random.choice(conddidans)
                return(b)
            else:
                conddidans=[at[0] for at in enemy.attacks if at[2]==0]
                b=random.choice(conddidans)
                return(b)
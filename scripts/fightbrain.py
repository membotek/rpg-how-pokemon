import pygame
from scripts import weapon
import random
def calcutedamage(weaponname,platackname,lastenatackname,enemy,player):
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
def calcutedefense(weaponname,enatackname,lastplatackname,player):
    defense=weapon.DAMAGES[weaponname]
    if lastplatackname=='block':
        defense*=2
    for i in weapon.GLOBALHAVEMOVMENTS[weaponname]:
        if i[0]==enatackname:
            defense*=i[2]
    a=random.randint(1,100)
    if a<=5:   # 5% crit
        defense*=0.5
    elif 6<=a<=95:   # 90% normal
        defense*=1
    elif a>=96:   # 5% lose
        defense*=2
    defense/=player.sheald*(player.level/4)
    return (defense)
    
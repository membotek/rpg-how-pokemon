import pygame
from scripts import weapon
import random
def calcutedamage(weaponname,platackname,lastenatackname,enemy,player):  # attack to enemy
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
    if lastplatackname=='block':
        damage*=0.5
    for i in enemy.attacks:
        if i[0]==enatackname:
    a=random.randint(1,100)
    if a<=5:   # 5% crit
        *=0.5
    elif 6<=a<=95:   # 90% normal
        *=1
    elif a>=96:   # 5% lose
        *=2
    return ()
    
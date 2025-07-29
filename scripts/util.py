import pygame
pygame.init()
import os
import csv

# load image and scale(yvelich)

def loadimage(path,scale=1,color=(0,0,0)):
    image=pygame.image.load(path).convert_alpha()
    w=image.get_width()
    h=image.get_height()
    image=pygame.transform.scale(image,(w*scale,h*scale))
    image=image.convert_alpha()
    if color!=False:
        image.set_colorkey((color))
    return(image)

def loadimages(dirpath,scale=1,color=(0,0,0)):
    images=[]
    filenames=os.listdir(dirpath)
    for i in filenames:
        filepath=dirpath+'/'+i
        images.append(loadimage(filepath,scale,color))
    return(images)
def loadbordermapfromcsv(path):
    nomberstr=-1
    nombersto=-1
    border=set()
    f=open(path)
    file=csv.reader(f,delimiter=',')
    for i in file:
        nomberstr+=1
        nombersto=-1
        for g in i:
            nombersto+=1
            if g=='395':
                border.add((nomberstr,nombersto))
    return(border)
def loadenemyfromcsv(path):
    nomberstr=-1
    nombersto=-1
    enemy=[]
    f=open(path)
    file=csv.reader(f,delimiter=',')
    for i in file:
        nomberstr+=1
        nombersto=-1
        for g in i:
            nombersto+=1
            if g=='391':
                enemy.append((nombersto,nomberstr,'spirit'))
            if g=='392':
                enemy.append((nombersto,nomberstr,'raccoon'))
            if g=='390':
                enemy.append((nombersto,nomberstr,'bamboo'))
    return(enemy)
def loadnameimages(path,scale):
    b={}
    for i in os.listdir(path):
        b[i[:-4]]=loadimage(path+'/'+i,scale)
    return(b)
def slise(path,size=64,nomber=(0,0),scale=1):
    image=loadimage(path,scale)
    subimage=image.subsurface([size*nomber[0]*scale,size*nomber[1]*scale,size*scale,size*scale])
    return(subimage)
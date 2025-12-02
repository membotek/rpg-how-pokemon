import pygame
pygame.init()
font=pygame.font.Font(None,56)
display=pygame.display.set_mode((64,64))
def make(colour,how_much):
    pygame.draw.rect(display,colour,(0,0,64,64))
    image=font.render(str(how_much),1,(0,0,0))
    display.blit(image,(image.get_width()-10,image.get_height()-10))
    pygame.image.save(display,str(how_much)+'.png')
for i in range(1,6):
    make((255,0,0),i)
import pygame,sys
from time import*
pygame.init()
screen= pygame.display.set_mode((600,600))
pygame.display.set_caption("ROCKET SHIP")
screen.fill("white")
player_x=250
player_y=250
keys=[False,False,False,False]
player=pygame.image.load("rocket.png")
bg=pygame.image.load("space.png")
pygame.display.update()
while True:
    screen.blit(bg,(0,0))
    screen.blit(player,(player_x,player_y))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
               keys[0]=True
            elif event.key==pygame.K_DOWN:
               keys[1]=True  
            elif event.key==pygame.K_LEFT:
               keys[2]=True 
            elif event.key==pygame.K_RIGHT:
               keys[3]=True   
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_UP:
               keys[0]=False
            elif event.key==pygame.K_DOWN:
               keys[1]=False 
            elif event.key==pygame.K_LEFT:
               keys[2]=False
            elif event.key==pygame.K_RIGHT:
               keys[3]=False
    if keys[0]:
       if player_y>0:
        player_y-=7   
    
    elif keys[1]:
       if player_y<450:
        player_y+=7  

    if keys[2]:
       if player_x>0:
        player_x-=7   
    
    elif keys[3]:
       if player_x<450:
        player_x+=7  

    player_y+=5
    sleep(0.05)  
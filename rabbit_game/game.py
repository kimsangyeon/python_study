# https://www.raywenderlich.com/24252/beginning-game-programming-for-teens-with-python

# 1 - Import library
import math
import random
import pygame
from pygame.locals import *

# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))

badtimer=100
badtimer1=0
badguys=[[640,100]]
healthvalue=194

# music
pygame.mixer.music.load('SuperMarioBros.mp3')
pygame.mixer.music.play(-1)

# FPS
FPS = 60
fpsClock = pygame.time.Clock()

# 3 - Load images
player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")
arrow = pygame.image.load("resources/images/bullet.png")
badguyimg1 = pygame.image.load("resources/images/badguy.png")
badguyimg=badguyimg1

# key input check
keys = [False, False, False, False]

# arrow
acc=[0,0]
arrows=[]

#player place(bunny)
playerpos = [100, 100]

running = 1
# 4 - keep looping through
while running:
    badtimer -= 1
    # 5 - clear the screen before drawing it again
    screen.fill(0)

    #grass paint
    for x in range(int(width/grass.get_width()+1)):
        for y in range(int(height/grass.get_height()+1)):
            screen.blit(grass,(x*100,y*100))
    screen.blit(castle,(0,30))
    screen.blit(castle,(0,135))
    screen.blit(castle,(0,240))
    screen.blit(castle,(0,345 ))

    # 6 - draw the screen elements
    mousePos = pygame.mouse.get_pos()
    # 좌표 (x1, y1) (x2, y2) math.atan2(y2 - y1, x2 - x1) = angle (radian)
    # 1 radian = 180 /math.pi = 57.29
    # 6.1 - Set player position and rotation
    radian = 180 / math.pi
    angle = math.atan2(mousePos[1] - playerpos[1], mousePos[0] - playerpos[0])
    playerrot = pygame.transform.rotate(player, 360 - angle * radian)
    playerpos1 = (playerpos[0] - playerrot.get_rect().width / 2, playerpos[1] - playerrot.get_rect().height / 2)
    screen.blit(playerrot, playerpos1)

    # 6.2 - Draw arrows
    for bullet in arrows:
        index=0
        velx=math.cos(bullet[0])*10
        vely=math.sin(bullet[0])*10
        bullet[1]+=velx
        bullet[2]+=vely
        if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
            arrows.pop(index)
        index+=1
        for projectile in arrows:
            arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
            screen.blit(arrow1, (projectile[1], projectile[2]))
    # 6.3 - Draw badgers
    if badtimer==0:
        badguys.append([640, random.randint(50,430)])
        badtimer=100-(badtimer1*2)
        if badtimer1>=35:
            badtimer1=35
        else:
            badtimer1+=5
    index=0
    for badguy in badguys:
        if badguy[0]<-64:
            badguys.pop(index)
        badguy[0]-=7
        index+=1
    for badguy in badguys:
        screen.blit(badguyimg, badguy)

    # 7 - update the screen
    pygame.display.flip()
    fpsClock.tick(FPS)
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
        # key down event
        if event.type == pygame.KEYDOWN:
            if event.key==K_w:
                keys[0]=True
            elif event.key==K_a:
                keys[1]=True
            elif event.key==K_s:
                keys[2]=True
            elif event.key==K_d:
                keys[3]=True
        # key up event
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w:
                keys[0]=False
            elif event.key==pygame.K_a:
                keys[1]=False
            elif event.key==pygame.K_s:
                keys[2]=False
            elif event.key==pygame.K_d:
                keys[3]=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            position=pygame.mouse.get_pos()
            acc[1]+=1
            arrows.append([math.atan2(position[1]-(playerpos1[1]),position[0]-(playerpos1[0])),playerpos1[0],playerpos1[1]])
    # player pos movement
    if keys[0]:
        playerpos[1]-=5
    elif keys[2]:
        playerpos[1]+=5
    if keys[1]:
        playerpos[0]-=5
    elif keys[3]:
        playerpos[0]+=5


# coding=utf8
import pygame
pygame.init()
pygame.mixer.music.load('SuperMarioBros.mp3')
pygame.mixer.music.play(-1)

display_width = 500
display_height = 500

screen = pygame.display.set_mode((display_width, display_height))

img = pygame.image.load('slide.png')
def myImg(x, y):
    screen.blit(img, (x, y))

x = (display_width * 0.5)
y = (display_height * 0.5)

finished = False
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    
    screen.fill((255, 255, 200))
    myImg(x, y)
    pygame.display.flip()

pygame.quit()
quit()
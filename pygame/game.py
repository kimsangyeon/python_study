import pygame
pygame.init()

screen = pygame.display.set_mode((400,300))
pygame.display.set_caption('파이게임')
finish = False

while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        pygame.display.flip()
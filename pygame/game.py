import pygame
pygame.init()

screen = pygame.display.set_mode((400,300))
pygame.display.set_caption('파이게임')
finish = False
color = (0, 128, 255)

x = 30
y = 30
clock = pygame.time.Clock()

while not finish:
    # 이벤트를 처리하는 부분 -> 키보드, 마우스 등의 이벤트 처리 코드가 들어감
    for event in pygame.event.get():
        # 윈도우의 닫기 버튼이 눌렸을 때, 프로그램을 종료하도록 처리
        if event.type == pygame.QUIT:
            finish = True

    # 게임의 상태를 업데이트하는 부분
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:
        if color == (0, 128, 255):
            color = (255, 255, 255)
        else:
            color = (0, 128, 255)
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3

    # 게임의 상태를 화면에 그려주는 부분 -> 화면을 지우고, 그리고, 업데이트하는 코드가 들어감
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
    pygame.display.flip()

    clock.tick(60)
    
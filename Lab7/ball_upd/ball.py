import pygame
pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Ball Game")
loop = True

#coordinates of the center
#первоначальная координата мячв
x = 300
y = 300
#borders
#Границы поля
up_limit = 25
down_limit = 575
left_limit = 25
right_limit = 575

#Создает объект Clock для управления FPS (кадры в секунду).
clock = pygame.time.Clock()

#Создает переменную loop, которая будет использоваться для основного игрового цикла.
while loop:
    pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    #checking if the arrow buttons are pressed and if the ball's center is leaving the borders
    if pressed[pygame.K_UP] and y >= up_limit:
        y -= 20
        y = max(y, up_limit)
    if pressed[pygame.K_DOWN] and y < down_limit:
        y += 20
        y = min(y, down_limit)
    if pressed[pygame.K_LEFT] and x > left_limit:
        x -= 20
        x = max(x, left_limit)
    if pressed[pygame.K_RIGHT] and x < right_limit:
        x += 20
        x = min(x, right_limit)

    screen.fill((255,255,255))
    pygame.draw.circle(screen, (255, 255, 50), (x,y), radius=25)

    #Обновление текущего экрана
    pygame.display.flip()
    #FPS до 60 кадров в секунду.
    clock.tick(60)
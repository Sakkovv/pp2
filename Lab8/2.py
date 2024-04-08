import pygame

def rectangle(x1, y1, x2, y2):
    x = min(x1, x2)
    y = min(y1, y2)
    w = abs(x1 - x2)
    z = abs(y1 - y2)
    return(x, y, w, z)

pygame.init()
screen = pygame.display.set_mode((600, 600))
another_layer = pygame.Surface((600, 600))

done = False
clock = pygame.time.Clock()
x1 = 10
y1 = 10
x2 = 10
y2 = 10

w = 100
z = 100
color = (99, 189, 153)
isMouseDown = False
screen.fill((255, 255, 255))

while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: #левая кнопк мыши
                    x1 = event.pos[0]
                    y1 = event.pos[1]
                    isMouseDown = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    isMouseDown = False
                    another_layer.blit(screen, (0, 0))

            if event.type == pygame.MOUSEMOTION:
                if isMouseDown:
                    x2 = event.pos[0]
                    y2 = event.pos[1]
                    screen.blit(another_layer, (0, 0))
                    pygame.draw.rect(screen, color, pygame.Rect(rectangle(x1, y1, x2, y2)), 1)


        pygame.display.flip()
        clock.tick(60)

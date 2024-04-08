import pygame

def rectangle(x1, y1, x2, y2):
    x = min(x1, y2)
    y = min(y1, y2)
    w = abs(x1-y2)
    z = abs(y1-y2)
    return(x, y, w, z)

pygame.init()
screen = pygame.display.set_mode((400, 300))
another_layer = pygame.Surface((400, 300))

done = False
clock = pygame.time.Clock()
x = 10
y = 10
w = 10
z = 10

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
              if event.button == 1: #левая кнопкf мыши
                 x1 = event.pos[0]
                 y1 = event.pos[1]
                 x2 = x1
                 y2 = y1
                 isMouseDown = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    isMouseDown = False
                #another_layer.blit(screen, (0, 0))

            if event.type == pygame.MOUSEMOTION:
                if isMouseDown:
                    x1 = x2
                    y1 = y2
                    x2 = event.pos[0]
                    y2 = event.pos[1]
                    #screen.blit(another_layer, (0, 0))
                    #pygame.draw.rect(screen, color, pygame.Rect(rectangle(x1, y1, x2, y2)), 1)
                    pygame.draw.line(screen, color, (x1, y1), (x2, y2))
        pygame.display.flip()
        clock.tick(60)

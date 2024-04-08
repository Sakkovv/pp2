import pygame 

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()

    drawing_color = (0, 0, 255)
    radius = 10
    drawing = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # ЛКМ
                    drawing = True
                elif event.button == 3:  # ПКМ
                    radius = max(1, radius - 1)  # маленький радиус карандаша
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # красный 'R'
                    drawing_color = (255, 0, 0)
                elif event.key == pygame.K_g:  # зеленый 'G'
                    drawing_color = (0, 255, 0)
                elif event.key == pygame.K_b:  # синий'B'
                    drawing_color = (0, 0, 255)      

        if drawing:
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(screen, drawing_color, pos, radius)
        
        pygame.display.flip()
        clock.tick(60)

main()
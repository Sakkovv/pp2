import pygame
pygame.init()
pygame.display.set_mode((600, 400))
f1Running = True
while f1Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            f1Running = False
  

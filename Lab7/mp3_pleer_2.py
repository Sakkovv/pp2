import pygame

pygame.init()
wind = pygame.display.set_mode((300, 200))
pygame.display.set_caption("Музыкальный Плеер")
music_file = "music_for_pleer"
pygame.mixer.music.load(music_file)

playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           playing = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_Space]:
        pygame.mixer.music.play()

    if keys[pygame.K_p]:
        pygame.mixer.music.pause()

    if keys[pygame.K_r]:
        pygame.mixer.music.unpause()


    if __name__ == "__main__":
        pygame.init()
        window = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("Музыкальный проигрыватель")
        music_file = "song.mp3"
        pygame.mixer.music.load(music_file)

        playing = True
        while playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE]:
                pygame.mixer.music.play()

            if keys[pygame.K_p]:
                pygame.mixer.music.pause()

            if keys[pygame.K_r]:
                pygame.mixer.music.unpause()

        pygame.quit()
  
import pygame
import os

pygame.init()

music_folder = "C:\\Муз"
music_files = [os.path.join(music_folder, f) for f in os.listdir(music_folder) if f.endswith(".mp3")]

pygame.mixer.init()
pygame.mixer.music.load(music_files[0])

running = True
current_track_index = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_n:
                current_track_index = (current_track_index + 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_track_index])
                pygame.mixer.music.play()
            elif event.key == pygame.K_p:
                current_track_index = (current_track_index - 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_track_index])
                pygame.mixer.music.play()
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()

pygame.quit()

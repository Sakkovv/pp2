import pygame
from game_object import GameObject 
from game_object import Point 

class Worm(GameObject):
    def __init__(self, tile_width):
        super().__init__([Point(20, 20)], (0, 0, 255), tile_width)
        self.DX = 1
        self.DY = 0     
    def increase(self, pos):
        self.points.append(Point(pos.X, pos.Y))

    def check_collision(self, screen_width, screen_height):
        head_position = self.points[0]  # Добавляем это
        # Проверяем столкновение с границами экрана
        if head_position.X < 0 or head_position.X >= screen_width or head_position.Y < 0 or head_position.Y >= screen_height:
            return True
        # Проверяем столкновение с самой змейкой (кроме головы)
        for point in self.points[1:]:
            if head_position.X == point.X and head_position.Y == point.Y:
                return True
        return False

    def move(self):

        for i in range(len(self.points) - 1, 0, -1):
            self.points[i].X = self.points[i - 1].X
            self.points[i].Y = self.points[i - 1].Y

        self.points[0].X += self.DX * self.tile_width
        self.points[0].Y += self.DY * self.tile_width

    def increase(self, pos):
        self.points.append(Point(pos.X, pos.Y))
        self.points.append(Point(pos.X, pos.Y))

    def process_input(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.DY != 1:  # Игнорируем движение вниз, если змея движется вверх
                    self.DX = 0
                    self.DY = -1
                elif event.key == pygame.K_DOWN and self.DY != -1:  # Игнорируем движение вверх, если змея движется вниз
                    self.DX = 0
                    self.DY = 1
                elif event.key == pygame.K_RIGHT and self.DX != -1:  # Игнорируем движение влево, если змея движется вправо
                    self.DX = 1
                    self.DY = 0
                elif event.key == pygame.K_LEFT and self.DX != 1:  # Игнорируем движение вправо, если змея движется влево
                    self.DX = -1
                    self.DY = 0

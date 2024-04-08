import pygame
from game_object import GameObject 
from game_object import Point 

class Wall(GameObject):
    def __init__(self, tile_width):
        super().__init__([],(255,0,0), tile_width)
        self.level = 1
        self.load_level()

    def load_level(self):
        f = open("levels/level{}.txt".format(self.level), "r")
        row = -1
        col = -1
        for line in f:
            row = row + 1
            col = -1
            for c in line:
                col = col + 1
                if c == '#':
                    self.points.append(Point(col * self.tile_width, row * self.tile_width))
        f.close()

    def next_level(self):
        self.points = []
        self.level = (self.level + 1) % 2
        self.load_level()

    """ def check_for_bondaries(self, game_over, screen_width, screen_height):
        if any((
            self.snake_head_pos[0] > screen_width-10
            or self.snake_head_pos[0] < 0,
            self.snake_head_pos[1] > screen_height-10
            or self.snake_head_pos[1] < 0
                )):
            game_over()
       
        for block in self.snake_body[1:]:
        if (block[0] == self.snake_head_pos[0] and
                block[1] == self.snake_head_pos[1]):
            game_over() """
            
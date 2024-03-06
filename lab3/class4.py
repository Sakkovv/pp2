import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f'x={self.x}  y={self.y}')

    def move(self, newx, newy):
        self.x = newx
        self.y = newy

    def dist(self, other_point):
        return math.sqrt((other_point.x - self.x)**2 + (other_point.y - self.y)**2)
    
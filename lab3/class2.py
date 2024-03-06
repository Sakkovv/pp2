class Shape:
    def __init__(self, length=0):
        self.length = length
        
    def area(self):
        return self.length

class Square(Shape):
    def __init__(self, length=0):
        super().__init__(length)

    def area(self):
        return self.length * self.length

shape = Shape(5)
print("shape:", shape.area())

square = Square(4)
print("square:", square.area())
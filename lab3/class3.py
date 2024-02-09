class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.length
    
rectangl = Rectangle(4, 5)
print('rectangle: ', rectangl.area())

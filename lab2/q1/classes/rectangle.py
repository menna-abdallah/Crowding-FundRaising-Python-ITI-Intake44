from .shape import Shape

class Rectangle(Shape):

    def __init__(self, name, color, length, width):
        super().__init__(name, color)
        self.length = length
        self.width = width
    
    def calculate_area(self):
     return self.length * self.width
        

    # def __init__(self, name, color, length, width):
    #     super().__init__(name, color, length)
    #     self.width = width
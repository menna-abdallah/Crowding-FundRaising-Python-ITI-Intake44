from .shape import Shape

class Square(Shape):
    def __init__(self, name, color, length):
        super().__init__(name, color)
        self.length = length

    
    def calculate_area(self):
        return self.length ** 2
    
    # def __init__(self, name, color, length):
    #     super().__init__(name, color, length)


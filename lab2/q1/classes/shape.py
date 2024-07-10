from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name, color):
        self.name = name
        self._color = color        
        
    
    def get_color(self):
        return self._name
        
    def set_color(self, name):
        self._color = name

    def get_color(self):
        return self._color
        
    def set_color(self, color):
        self._color = color
    

    
    @abstractmethod
    def calculate_area(self):
        pass


    #   def __init__(self, name, color, length):
    #     self.name = name
    #     self._color = color
    #     self.length = length

    # def get_length(self):
    #     return self.length
    
    # def set_length(self, length):
    #     self.length = length
import math

class Figure:
    unit = 'cm'

    def calculate_area(self):
        raise NotImplementedError

    def info(self):
        raise NotImplementedError


class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius
    @property
    def radius(self): 
        return self.__radius
    @radius.setter 
    def radius(self, value): # Cеттер 2
        self.__radius = value
    
    def calculate_area(self):
        return round(math.pi * self.__radius ** 2, 2)

    def info(self):
        print(f"Circle radius: {self.__radius}{self.unit}, area: {self.calculate_area()}{self.unit}")


class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        self.__side_a = side_a
        self.__side_b = side_b

    def calculate_area(self):
        return round(0.5 * self.__side_a * self.__side_b, 2)

    def info(self):
        print(f"RightTriangle side a: {self.__side_a}{self.unit}, side b: {self.__side_b}{self.unit}, "
              f"area: {self.calculate_area()}{self.unit}")


nono1 = Circle(2)
nono2 = Circle(30)

nene1 = RightTriangle(5, 8)
nene2 = RightTriangle(3, 4)
nene3 = RightTriangle(6, 10)

figures = [nono1, nono2, nene1, nene2, nene3]

for figure in figures:
    figure.info()





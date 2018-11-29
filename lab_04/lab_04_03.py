from math import pi


class Geometric:

    def calculate_area(self):
        print("Calculating area")


class Square(Geometric):

    def __init__(self, a):
        self.side = a

    def _perimeter(self):
        print("Perimeter of Square {}: {}\n".format(self.side, self.side * 4))

    def calculate_area(self):
        print("Area of Square {}: {}\n".format(self.side, pow(self.side, 2)))


class Circle(Geometric):

    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        print("Area of Circle {}: {}\n".format(self.__radius, pi * pow(self.__radius, 2)))


geom = Geometric()
geom.calculate_area()
sq = Square(5)
sq.calculate_area()
sq._perimeter()
print("Check subclass: ", issubclass(Square, Geometric))
print("Check instance sq->Square: ", isinstance(sq, Square))
print("Check instance sq->Geometric: ", isinstance(sq, Geometric))
print("Check instance sq->dict: ", isinstance(sq, dict))
print("Geometric.__bases__: ", Geometric.__bases__)
print("Square.__bases__: ", Square.__bases__)

circle = Circle(3)
circle.calculate_area()

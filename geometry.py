"""Класс для работы с геометрическими фигурами:
Разработайте класс "Shape", представляющий геометрическую фигуру.
Создайте подклассы для различных фигур, таких как круг, прямоугольник и треугольник.
Каждый подкласс должен иметь методы для вычисления площади и периметра, а также конструкторы,
принимающие необходимые параметры (например, радиус, стороны)."""
from math import pi, sqrt


class Shape:
    def __init__(self):
        self.s = 0
        self.p = 0

    def get_perimeter(self):
        print(self.p)

    def get_square(self):
        print(self.s)

    def __eq__(self, other):
        return self.s == other.s

    def __lt__(self, other):
        return self.s < other.s

    def __le__(self, other):
        return self.s <= other.s


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.r = radius
        self.s = self.r ** 2 * pi
        self.p = self.r * pi * 2


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
        self.s = self.length * self.width
        self.p = (self.length + self.width) * 2


class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
        self.p = self.a + self.b + self.c
        self.pp = (self.a + self.b + self.c) / 2
        self.s = sqrt(self.pp*(self.pp - self.a)*(self.pp - self.b)*(self.pp - self.c))


if __name__ == '__main__':
    c = Circle(2)
    c2 = Circle(4)
    r = Rectangle(2, 5)
    r2 = Rectangle(2, 5)
    r3 = Rectangle(5, 2)
    t = Triangle(3, 4, 5)

    print(c > c2)
    print(r <= r2)
    print(r3 >= t)
    c2.get_square()
    r3.get_square()
    t.get_square()

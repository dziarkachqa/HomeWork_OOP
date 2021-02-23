'''Write a program that defines a shape class with a constructor
that gives value to w (width) and h(height) and not implemented area() method.
Define two sub-classes Triangle and Rectangle, implement area method,
it should return area of the figure according to geometry rules (google formulas).
Below instantiate two objects a triangle and a rectangle and call the area() function
in this two varibles.'''


class Shape:
    def __init__(self, w, h):
        self.w = w
        self.h = h


class Triangle(Shape):
    def area(self):
        area = (1 / 2) * (self.w * self.h)
        return int(area)


class Rectangle(Shape):
    def area(self):
        area = (self.w * self.h)
        return int(area)


triangle = Triangle(w=10, h=12)
rectangle = Rectangle(w=10, h=12)

print(triangle.area())  # -> 60
print(rectangle.area())  # -> 120

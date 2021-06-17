class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point(Shape):
    pass


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def contains(self, point):
        return ((point.x - self.x) ** 2 + (point.y - self.y) ** 2) <= self.radius ** 2


point = Point(50, 50)
circle = Circle(50, 50, 100)
print(circle.contains(point))

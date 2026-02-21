import math
class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = [[' '] * width for _ in range(height)]

    def set_pixel(self, row, col, char='*'):
        if 0 <= row < self.height and 0 <= col < self.width:
            self.data[row][col] = char

    def clear_canvas(self):
        self.data = [[' '] * self.width for _ in range(self.height)]

    def v_line(self, x, y, w, **kargs):
        for i in range(x, x + w):
            self.set_pixel(i, y, **kargs)

    def h_line(self, x, y, h, **kargs):
        for i in range(y, y + h):
            self.set_pixel(x, i, **kargs)

    def line(self, x1, y1, x2, y2, **kargs):
        slope = (y2 - y1) / (x2 - x1)
        for y in range(y1, y2):
            x = int(slope * y)
            self.set_pixel(x, y, **kargs)

    def display(self):
        print("\n".join("".join(row) for row in self.data))


class Shape:
    def paint(self, canvas):
        raise NotImplementedError("paint() not implemented")

class Rectangle(Shape):
    def __init__(self, length, width, x, y, char='*'):
        self.length = length
        self.width = width
        self.x = x
        self.y = y
        self.char = char

    def boundary_points(self):
        points = []
        n = 4
        for i in range(n):
            points.append((self.x + i * self.length / n, self.y))
        for i in range(n):
            points.append((self.x + self.length, self.y + i * self.width / n))
        for i in range(n):
            points.append((self.x + self.length - i * self.length / n, self.y + self.width))
        for i in range(n):
            points.append((self.x, self.y + self.width - i * self.width / n))
        return points

    def paint(self, canvas):
        for x, y in self.boundary_points():
            canvas.set_pixel(int(y), int(x), char=self.char)


class Circle(Shape):
    def __init__(self, radius, x, y, char='o'):
        self.radius = radius
        self.x = x
        self.y = y
        self.char = char

    def boundary_points(self):
        points = []
        n = 
        for i in range(n):
            theta = 2 * math.pi * i / n
            points.append((
                self.x + self.radius * math.cos(theta),
                self.y + self.radius * math.sin(theta)
            ))
        return points

    def paint(self, canvas):
        for x, y in self.boundary_points():
            canvas.set_pixel(int(y), int(x), char=self.char)


class Triangle(Shape):
    def __init__(self, base, height, x, y, char='^'):
        self.base = base
        self.height = height
        self.x = x
        self.y = y
        self.char = char

    def boundary_points(self):
        points = []
        n = 5
        for i in range(n):
            points.append((self.x + i * self.base / n, self.y))
        for i in range(n):
            points.append((self.x, self.y + i * self.height / n))
        for i in range(n):
            t = i / n
            points.append((self.x + t * self.base, self.y + t * self.height))
        return points

    def paint(self, canvas):
        for x, y in self.boundary_points():
            canvas.set_pixel(int(y), int(x), char=self.char)

class CompoundShape(Shape):
    def __init__(self, shapes):
        self.shapes = shapes

    def paint(self, canvas):
        for shape in self.shapes:
            shape.paint(canvas)

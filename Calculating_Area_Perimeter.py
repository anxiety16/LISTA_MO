class shape:
    def __init__(self):
        self.unit = "meters"
    def area(self):
        pass
    def perimeter(self):
        pass
    def display(self):
        pass

class circle(shape):
    def __init__(self, radius):
        self.unit = "meters"
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def display(self):
        print(f'Circle:\n'
              f'Radius = {self.radius} {self.unit}\n'
              f'Area = {self.area()} {self.unit} squared \n'
              f'Perimeter = {self.perimeter()} {self.unit}')

class square(shape):
    def __init__(self, side):
        self.unit = "meters"
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

    def display(self):
        print(f'Square:\n'
              f'Sides = {self.side} {self.unit}\n'
              f'Area = {self.area()} {self.unit} squared\n'
              f'Perimeter = {self.perimeter()} {self.unit}')

class triangle(shape):
    def __init__(self, base, height, side):
        self.unit = "meters"
        self.base = base
        self.height = height
        self.side = side

    def area(self):
        return (self.base * self.height) / 2

    def perimeter(self):
        return self.side + self.base + self.height

    def display(self):
        print(f'triangle:\n'
              f'Side A = {self.side} {self.unit}\n'
              f'Base = {self.base} {self.unit}\n'
              f'Height = {self.height} {self.unit}\n'
              f'Area = {self.area()} {self.unit} squared\n'
              f'Perimeter = {self.perimeter()} {self.unit}')

class rectangle(shape):
    def __init__ (self,length, width):
        self.unit = "meters"
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width) * 2

    def display(self):
        print(f'rectangle:\n'
              f'length = {self.length} {self.unit}\n'
              f'width = {self.width} {self.unit}\n'
              f'Area = {self.area()} {self.unit} squared\n'
              f'Perimeter = {self.perimeter()} {self.unit}')



circle = circle(1)
circle.display()
square = square(3)
square.display()
triangle = triangle(5,5,1)
triangle.display()
rectangle = rectangle(5,5)
rectangle.display()

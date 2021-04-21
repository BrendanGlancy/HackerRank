import math
class Shape(object):
    # Shape object
    
    def getArea(self):
        pass
    
    def permeter(self):
        pass
    
class Square(Shape):
    # Square Shape
    
    def __init__(self, side_length):
        self.side = side_length
        
    def getArea(self):
        # Seem to want me to round up so math.ceil
        return math.ceil(self.side * self.side)
    
    def perimeter(self):
        return self.side * 4
    
class Rectangle(Shape):
    # Rectangle Shape
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def getArea(self):
        # a = l * w
        return math.ceil(self.length * self.width)
    
    def perimeter(self):
        # P=2(l+w)
        return 2 * self.length + 2 * self.width
    
class Circle(Shape):
    # Circle Shape
    
    def __init__(self, radius):
        self.radius = radius
        
    def getArea(self):
        # A = pi r^2
        return math.ceil(math.pi * self.radius * self.radius)
    
    def perimeter(self):
        # C=2πr
        return round(2 * math.pi * self.radius)

if __name__ == '__main__':
    radius = float(input())
    c1 = Circle(radius)
    print(c1.getArea())
    
    dims = input().split(" ")
    width = float(dims[0])
    height = float(dims[1])
    r1 = Rectangle(width, height)
    print(r1.getArea())
    
    radius = float(input())
    c2 = Circle(radius)
    print(c2.getArea())
    
    width = float(input())
    s1 = Square(width)
    print(s1.getArea())
    
    dims = input().split(" ")
    width = float(dims[0])
    height = float(dims[1])
    r2 = Rectangle(width, height)
    print(r2.getArea())

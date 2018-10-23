class Rectangle(object):
    def __init__(self,width,height):
        self.width = width
        self.height = height     
    def area(self):
        return self.width * self.height
class Square(object):
    def __init__(self,width):
        self.width  = width
    def area(self):
        return self.width * self.width 
class Ellipse(object):
    def __init__(self,bcz,bdz):
        self.bcz = bcz
        self.bdz = bdz        
    def area(self):
        return self.bcz*self.bdz*3.14
class Circle(object):
    def __init__(self,radius):
        self.radius = radius       
    def area(self):
        return self.radius*self.radius*3.14
def compute_area(shapes):
    return sum([x.area()for x in shapes])

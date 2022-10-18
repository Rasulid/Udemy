from shelve import Shelf


class Shape :
    def __init__(self):
        print('Shepe created')

    def draw(self):
        print('Drawing a shepe')

    def area(self):
        print('Calc area')

    def perimetr(self):
        print('Calc perimetr')

shape = Shape()
print(shape)


class Rectangle(Shape):
    def __init__(self , high , width):
        Shape.__init__(self)
        self.high = high
        self.width = width

        print('Rectengle create')

        Shape.area(self)
    def area(self):
        return self.width * self.high
    
    def perimetr(self):
        return 2 * (self.high + self.width)

    def draw(self):
        print(f"Drawing rectangle with width = {self.width}  and high = {self.high}")

rect = Rectangle(10 , 15)
print(rect.draw() , rect.perimetr() , rect.area() , sep="\n")

import math
class Triangle (Shape):

    def __init__(self , a , b , c):
        super().__init__()

        self.a = a
        self.b = b 
        self.c = c 

        print('Triangle Created')

    def draw(self):
        print(f'Drawing triangle whith sides ={self.a} , {self.b} , {self.c}')
        return super().draw()

            

    
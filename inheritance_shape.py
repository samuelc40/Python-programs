
class  Shape:
    def __init__(self, color, area=None):
        self.color = color
        self.area = area

class CircleShape(Shape):
    def circle_area(self):
        pi = 3.14
        radius = int(input("Enter the radius of the circle: "))
        circle_area = pi * radius ** 2
        self.area = circle_area
        print("Area of the circle is : ", self.area, "\nAnd the color is : ", self.color)

class TriangleShape(Shape):
    def triangle_area(self):
        breadth = int(input('Enter the breadth of the triangle: '))
        height = int(input('Enter the height of the triangle: '))

        if breadth is None or height is None:
            print("Area cannot be calculated !")
        else:
            triangle_area = 1/2*(breadth*height)
            self.area = triangle_area
            print("Area of the triangle is : ", self.area, "\nAnd the color is : ", self.color)

class RectangleShape(Shape):
    def rectangle_area(self):
        length = int(input("Enter the length of the rectangle: "))
        Width = int(input("Enter the Width of the rectangle: "))
        # height = int(input("Enter the height of the rectangle: "))

        rectangle_area = length * Width
        self.area = rectangle_area
        print("Area of the rectangle is : ", self.area, "\nAnd the color is : ", self.color)



        


obj = CircleShape('red')

# obj.circle_area()

obj2 = TriangleShape('Green')
# obj2.triangle_area()

obj3 = RectangleShape('Blue')
obj3.rectangle_area()

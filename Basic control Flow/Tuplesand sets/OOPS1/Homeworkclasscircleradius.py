class Circle:
    pi=3.14
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return round(self.pi * self.radius ** 2, 2)
    
    def circumference(self):
        return round(2 * self.pi * self.radius, 2)

radius= int(input("Enter the radius of the circle: "))
circle = Circle(radius)
print("Area of the circle:", circle.area())
print("Circumference of the circle:", circle.circumference())
class circle:
    pie=3.14
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return self.pie*self.radius**2
    def perimeter(self):
        return 2*self.pie*self.radius
c=circle(5)
print(c.area())
print(c.perimeter())    


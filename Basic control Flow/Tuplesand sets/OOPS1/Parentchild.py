class parent:
    def __init__(self, name):
        self.name = name
class child(parent):  
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    def display(self):
        print("Name:", self.name,"Age:", self.age,sep=" ")
        
c = child("Alice", 10)
c.display()